#!/usr/bin/env python3
"""
Google Calendar API Client

Usage:
  calendar_client.py auth              - Authorize with Google
  calendar_client.py today             - Show today's events
  calendar_client.py list [--days N]   - List upcoming events
  calendar_client.py free [--date D]   - Find free time slots
  calendar_client.py create [options]  - Create an event
"""

import os
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path

# Google API imports
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Install required packages: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 
          'https://www.googleapis.com/auth/calendar.events']
CONFIG_DIR = Path.home() / '.config' / 'calendar'
CREDS_FILE = CONFIG_DIR / 'credentials.json'
TOKEN_FILE = CONFIG_DIR / 'token.json'

def get_credentials():
    """Get valid credentials, refreshing or re-authorizing as needed."""
    creds = None
    
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDS_FILE.exists():
                print(json.dumps({
                    "error": "No credentials.json found",
                    "setup": "Download OAuth client credentials from Google Cloud Console",
                    "path": str(CREDS_FILE)
                }))
                sys.exit(1)
            
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        TOKEN_FILE.write_text(creds.to_json())
        os.chmod(TOKEN_FILE, 0o600)
    
    return creds

def get_service():
    """Build the Calendar API service."""
    creds = get_credentials()
    return build('calendar', 'v3', credentials=creds)

def list_events(days=1, date_str=None):
    """List events for the specified period."""
    service = get_service()
    
    if date_str:
        start = datetime.fromisoformat(date_str).replace(hour=0, minute=0, second=0)
    else:
        start = datetime.now().replace(hour=0, minute=0, second=0)
    
    end = start + timedelta(days=days)
    
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start.isoformat() + 'Z',
        timeMax=end.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])
    
    result = []
    for event in events:
        start_time = event['start'].get('dateTime', event['start'].get('date'))
        end_time = event['end'].get('dateTime', event['end'].get('date'))
        
        result.append({
            'id': event['id'],
            'title': event.get('summary', 'No title'),
            'start': start_time,
            'end': end_time,
            'location': event.get('location', ''),
            'attendees': [a['email'] for a in event.get('attendees', [])],
            'status': event.get('status', 'confirmed')
        })
    
    print(json.dumps(result, indent=2))

def find_free_time(date_str=None, duration_minutes=60):
    """Find free time slots on the specified date."""
    service = get_service()
    
    if date_str:
        day = datetime.fromisoformat(date_str)
    else:
        day = datetime.now()
    
    # Business hours: 9 AM to 6 PM
    work_start = day.replace(hour=9, minute=0, second=0, microsecond=0)
    work_end = day.replace(hour=18, minute=0, second=0, microsecond=0)
    
    # Get events for the day
    events_result = service.events().list(
        calendarId='primary',
        timeMin=work_start.isoformat() + 'Z',
        timeMax=work_end.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    
    events = events_result.get('items', [])
    
    # Find gaps
    free_slots = []
    current = work_start
    
    for event in events:
        event_start = datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')).replace('Z', '+00:00'))
        event_end = datetime.fromisoformat(event['end'].get('dateTime', event['end'].get('date')).replace('Z', '+00:00'))
        
        # Naive comparison (assumes same timezone)
        event_start = event_start.replace(tzinfo=None)
        event_end = event_end.replace(tzinfo=None)
        
        if current < event_start:
            gap_minutes = (event_start - current).total_seconds() / 60
            if gap_minutes >= duration_minutes:
                free_slots.append({
                    'start': current.isoformat(),
                    'end': event_start.isoformat(),
                    'duration_minutes': int(gap_minutes)
                })
        
        current = max(current, event_end)
    
    # Check time after last event
    if current < work_end:
        gap_minutes = (work_end - current).total_seconds() / 60
        if gap_minutes >= duration_minutes:
            free_slots.append({
                'start': current.isoformat(),
                'end': work_end.isoformat(),
                'duration_minutes': int(gap_minutes)
            })
    
    print(json.dumps(free_slots, indent=2))

def create_event(title, start_str, duration_minutes=60, description='', location=''):
    """Create a new calendar event."""
    service = get_service()
    
    start = datetime.fromisoformat(start_str)
    end = start + timedelta(minutes=duration_minutes)
    
    event = {
        'summary': title,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
    }
    
    event = service.events().insert(calendarId='primary', body=event).execute()
    
    print(json.dumps({
        'status': 'created',
        'id': event['id'],
        'link': event.get('htmlLink', '')
    }))

def auth():
    """Run the authorization flow."""
    get_credentials()
    print(json.dumps({'status': 'authorized', 'token_path': str(TOKEN_FILE)}))

if __name__ == '__main__':
    args = sys.argv[1:]
    
    if not args or args[0] == 'help':
        print(__doc__)
        sys.exit(0)
    
    cmd = args[0]
    
    try:
        if cmd == 'auth':
            auth()
        elif cmd == 'today':
            list_events(days=1)
        elif cmd == 'list':
            days = 7
            date_str = None
            for i, arg in enumerate(args[1:]):
                if arg == '--days' and i + 2 < len(args):
                    days = int(args[i + 2])
                if arg == '--date' and i + 2 < len(args):
                    date_str = args[i + 2]
            list_events(days=days, date_str=date_str)
        elif cmd == 'free':
            date_str = None
            for i, arg in enumerate(args[1:]):
                if arg == '--date' and i + 2 < len(args):
                    date_str = args[i + 2]
            find_free_time(date_str=date_str)
        elif cmd == 'create':
            # Parse create options
            title = None
            start = None
            duration = 60
            description = ''
            location = ''
            for i, arg in enumerate(args[1:]):
                if arg == '--title' and i + 2 < len(args):
                    title = args[i + 2]
                if arg == '--start' and i + 2 < len(args):
                    start = args[i + 2]
                if arg == '--duration' and i + 2 < len(args):
                    duration = int(args[i + 2])
                if arg == '--description' and i + 2 < len(args):
                    description = args[i + 2]
                if arg == '--location' and i + 2 < len(args):
                    location = args[i + 2]
            
            if not title or not start:
                print(json.dumps({'error': 'Required: --title and --start'}))
                sys.exit(1)
            
            create_event(title, start, duration, description, location)
        else:
            print(f"Unknown command: {cmd}")
            print(__doc__)
            sys.exit(1)
    except HttpError as e:
        print(json.dumps({'error': str(e)}))
        sys.exit(1)
