import smtplib
import imaplib

import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import os

from mail import Mail


class Mailer():

    def __init__(self, myAddr, myPswrd):
        self.Addr = myAddr
        self.Pswrd = myPswrd
        self.server = "smtp.gmail.com"
        self.portOut = 587
        self.portIn = 993

    def sendMail(self, other, subject, body):
    
        message = MIMEMultipart()
        message["From"] = self.Addr
        message["To"] = other
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        try:
            with smtplib.SMTP(self.server, self.portOut) as server:
                server.starttls()
                server.login(self.Addr, self.Pswrd)
                server.sendmail(self.Addr, other, message.as_string())
            return("Email sent successfully!")
        except Exception as e:
            return(f"Error sending email: {e}")

    def decode_email_subject(self, subject):
        """Decode email subject with proper encoding."""
        decoded_subject = decode_header(subject)[0][0]
        if isinstance(decoded_subject, bytes):
            try:
                return decoded_subject.decode()
            except:
                return decoded_subject.decode("utf-8", errors="ignore")
        return decoded_subject

    def get_email_body(self, msg):
        """Extract email body (plain text preferred, then HTML)."""
        try:
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        return part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    elif part.get_content_type() == "text/html":
                        return part.get_payload(decode=True).decode("utf-8", errors="ignore")
            else:
                return msg.get_payload(decode=True).decode("utf-8", errors="ignore")
        except Exception as e:
            print(f"Error decoding email body: {e}")
            return ""

    def read_emails(self):
        # Gmail IMAP settings
        search_query = 'FROM "afrika.mcclintock@outlook.com"'  # Filter for emails from your Outlook account

        try:
            # Connect to Gmail IMAP server
            imap = imaplib.IMAP4_SSL(self.server, self.portIn)
            imap.login(self.Addr, self.Pswrd)
            
            # Select the inbox
            imap.select("INBOX")
            
            # Search for emails
            status, messages = imap.search(None, search_query)
            email_ids = messages[0].split()
            
            if not email_ids:
                #print("No emails found matching the query.")
                imap.logout()
                return
            
            #print(f"Found {len(email_ids)} emails:")
            readMail = []
            # Limit to 10 most recent emails
            for email_id in email_ids[-10:]:
                status, msg_data = imap.fetch(email_id, "(RFC822)")
                email_msg = email.message_from_bytes(msg_data[0][1])
                
                # Extract details
                from_email = email_msg["from"] or "Unknown"
                subject = self.decode_email_subject(email_msg["subject"] or "No Subject")
                body = self.get_email_body(email_msg)
                id = email_id
                
                readMail.append(Mail(from_email, subject, body, id))
            
            imap.logout()

            return(readMail)
        except Exception as e:
            print(f"Error reading emails: {e}")
            return
    
    def delete_emails(self, search_query='FROM "afrika.mcclintock@outlook.com"', emailID = None):
    # Gmail IMAP settings

        try:
            # Connect to Gmail IMAP server
            imap = imaplib.IMAP4_SSL(self.server, self.portIn)
            imap.login(self.Addr, self.Pswrd)
            
            # Select the inbox
            imap.select("INBOX")
            
            # Search for emails
            status, messages = imap.search(None, search_query)
            email_ids = messages[0].split()
            
            if not email_ids:
                print("No emails found matching the query.")
                imap.logout()
                return
            
            print(f"Found {len(email_ids)} emails to delete:")
            operatedEmailIDs = []
            for email_id in email_ids:
                # Fetch email details for display
                status, msg_data = imap.fetch(email_id, "(RFC822)")
                email_msg = email.message_from_bytes(msg_data[0][1])
                
                from_email = email_msg["from"] or "Unknown"
                subject = self.decode_email_subject(email_msg["subject"] or "No Subject")
                
                deleteAll = False
                if(emailID == None):
                    deleteAll = True

                if(email_id.decode() == emailID or deleteAll):
                    #print(f"\nMarking for deletion - Email ID: {email_id.decode()}")
                    #print(f"From: {from_email}")
                    #print(f"Subject: {subject}")
                    
                    # Mark email for deletion
                    imap.store(email_id, "+FLAGS", "\\Deleted")
                    operatedEmailIDs.append(email_id)
            
            # Permanently delete marked emails
            imap.expunge()
            print(f"\nDeleted {len(operatedEmailIDs)} emails.")
            
            imap.logout()
        except Exception as e:
            print(f"Error deleting emails: {e}")
            if 'imap' in locals():
                imap.logout()