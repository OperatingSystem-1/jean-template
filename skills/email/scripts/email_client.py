#!/usr/bin/env python3
"""
Email client for reading, searching, and forwarding emails via IMAP/SMTP.
Credentials are loaded from ~/.config/email/credentials.json
"""

import argparse
import imaplib
import smtplib
import email
import json
import re
from email.header import decode_header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "email" / "credentials.json"


def load_config():
    """Load email configuration from credentials file."""
    if not CONFIG_PATH.exists():
        print(f"Error: Credentials file not found at {CONFIG_PATH}")
        print("Create it with: server, username, password, email fields")
        raise SystemExit(1)
    with open(CONFIG_PATH) as f:
        return json.load(f)


def decode_subject(subject):
    """Decode email subject."""
    if subject is None:
        return "(No Subject)"
    try:
        decoded_list = decode_header(subject)
        result = ""
        for decoded, charset in decoded_list:
            if isinstance(decoded, bytes):
                try:
                    result += decoded.decode(charset or 'utf-8', errors='ignore')
                except LookupError:
                    result += decoded.decode('utf-8', errors='ignore')
            else:
                result += str(decoded)
        return result
    except Exception:
        return str(subject)


def get_body(msg):
    """Extract body from email message."""
    body = ""
    html_body = ""

    if msg.is_multipart():
        for part in msg.walk():
            ct = part.get_content_type()
            if ct == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    body = payload.decode(errors='ignore')
            elif ct == "text/html":
                payload = part.get_payload(decode=True)
                if payload:
                    html_body = payload.decode(errors='ignore')
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors='ignore')

    return body, html_body


def extract_verification_code(text):
    """Extract verification code from email body."""
    # Look for 6-digit codes in styled divs
    div_pattern = r'<div[^>]*>\s*(\d{6})\s*</div>'
    matches = re.findall(div_pattern, text, re.IGNORECASE)
    if matches:
        return matches[0]

    # Look for codes after keywords
    code_pattern = r'(?:code|Code|verification)[:\s]*(\d{4,6})'
    matches = re.findall(code_pattern, text, re.IGNORECASE)
    if matches:
        return matches[0]

    # Fallback: standalone 6-digit numbers (excluding color codes)
    all_codes = re.findall(r'(?<!#)(?<![0-9a-fA-F])\b(\d{6})\b', text)
    if all_codes:
        return all_codes[0]

    return None


def list_emails(limit=10):
    """List recent emails."""
    config = load_config()

    mail = imaplib.IMAP4_SSL(config['server'])
    mail.login(config['username'], config['password'])
    mail.select('INBOX')

    status, messages = mail.search(None, 'ALL')
    mail_ids = messages[0].split()

    print(f"Total emails: {len(mail_ids)}")
    print("-" * 60)

    for i, mail_id in enumerate(reversed(mail_ids[-limit:])):
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        subject = decode_subject(msg["Subject"])
        from_ = msg.get("From", "Unknown")
        date = msg.get("Date", "Unknown")

        print(f"[{mail_id.decode()}] {subject}")
        print(f"    From: {from_}")
        print(f"    Date: {date}")
        print()

    mail.logout()


def read_email(email_id):
    """Read a specific email."""
    config = load_config()

    mail = imaplib.IMAP4_SSL(config['server'])
    mail.login(config['username'], config['password'])
    mail.select('INBOX')

    status, msg_data = mail.fetch(str(email_id).encode(), '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])

    subject = decode_subject(msg["Subject"])
    from_ = msg.get("From", "Unknown")
    date = msg.get("Date", "Unknown")
    body, html_body = get_body(msg)

    print(f"Subject: {subject}")
    print(f"From: {from_}")
    print(f"Date: {date}")
    print("-" * 60)
    print(body if body else html_body)

    mail.logout()


def search_emails(subject_filter=None, from_filter=None, extract_code=False, limit=10):
    """Search emails and optionally extract verification codes."""
    config = load_config()

    mail = imaplib.IMAP4_SSL(config['server'])
    mail.login(config['username'], config['password'])
    mail.select('INBOX')

    status, messages = mail.search(None, 'ALL')
    mail_ids = messages[0].split()
    
    count = 0
    for mail_id in reversed(mail_ids):
        if count >= limit:
            break
            
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        subject = decode_subject(msg["Subject"])
        from_ = msg.get("From", "")

        if subject_filter and subject_filter.lower() not in subject.lower():
            continue
        if from_filter and from_filter.lower() not in from_.lower():
            continue

        body, html_body = get_body(msg)

        print(f"[{mail_id.decode()}] {subject}")
        print(f"    From: {from_}")
        print(f"    Date: {msg.get('Date')}")

        if extract_code:
            code = extract_verification_code(html_body or body)
            if code:
                print(f"    Verification Code: {code}")
        print()
        count += 1

    mail.logout()


def forward_email(email_id, to_address):
    """Forward an email to another address."""
    config = load_config()

    mail = imaplib.IMAP4_SSL(config['server'])
    mail.login(config['username'], config['password'])
    mail.select('INBOX')

    status, msg_data = mail.fetch(str(email_id).encode(), '(RFC822)')
    original_msg = email.message_from_bytes(msg_data[0][1])

    subject = decode_subject(original_msg["Subject"])
    body, html_body = get_body(original_msg)

    forward_msg = MIMEMultipart()
    forward_msg['From'] = config['email']
    forward_msg['To'] = to_address
    forward_msg['Subject'] = f"Fwd: {subject}"

    forward_text = f"""
---------- Forwarded message ----------
From: {original_msg.get('From')}
Date: {original_msg.get('Date')}
Subject: {subject}

{body if body else html_body}
"""
    forward_msg.attach(MIMEText(forward_text, 'plain'))

    mail.logout()

    smtp_server = config.get('smtp_server', config['server'])
    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.login(config['username'], config['password'])
    smtp.send_message(forward_msg)
    smtp.quit()

    print(f"Forwarded '{subject}' to {to_address}")


def main():
    parser = argparse.ArgumentParser(description='Email client for IMAP/SMTP')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    list_parser = subparsers.add_parser('list', help='List recent emails')
    list_parser.add_argument('--limit', type=int, default=10)

    read_parser = subparsers.add_parser('read', help='Read a specific email')
    read_parser.add_argument('--id', type=int, required=True)

    search_parser = subparsers.add_parser('search', help='Search emails')
    search_parser.add_argument('--subject', help='Filter by subject')
    search_parser.add_argument('--from', dest='from_addr', help='Filter by sender')
    search_parser.add_argument('--extract-code', action='store_true')
    search_parser.add_argument('--limit', type=int, default=10)

    forward_parser = subparsers.add_parser('forward', help='Forward an email')
    forward_parser.add_argument('--id', type=int, required=True)
    forward_parser.add_argument('--to', required=True)

    args = parser.parse_args()

    if args.command == 'list':
        list_emails(args.limit)
    elif args.command == 'read':
        read_email(args.id)
    elif args.command == 'search':
        search_emails(args.subject, args.from_addr, args.extract_code, args.limit)
    elif args.command == 'forward':
        forward_email(args.id, args.to)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
