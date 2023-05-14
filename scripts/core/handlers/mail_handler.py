import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str

class EmailHandler:
    
    def __init__(self):
        self.sender_email = os.environ.get("MAIL_USERNAME")
        self.sender_password = os.environ.get("MAIL_PASSWORD")
    
    def send_email(self, email: Email):
        # Create a multipart message
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = email.rec_email
        message["Subject"] = email.subject
        
        # Add the body to the email
        message.attach(MIMEText(email.body, "plain"))
        
        try:
            # Create a secure connection to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            
            # Login to the sender's email account
            server.login(self.sender_email, self.sender_password)
            
            # Send the email
            server.send_message(message)
            
            # Close the connection
            server.quit()
            
            return {"message": "Email sent successfully"}
        
        except Exception as e:
            print(e)
            return {"message": str(e.args)}
