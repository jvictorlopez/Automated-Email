import smtplib
import ssl
from email.message import EmailMessage
import json

# Define email sender
email_sender = 'your-email@domain.com'
email_password = 'your-password'

# Load recipients from JSON file
with open('recipients.json', 'r') as f:
    recipients = json.load(f)

# Set the subject and body of the email
subject = 'Congratulations on completing the 5G Networks course'

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    # Loop through the recipients
    for name, email_receiver in recipients.items():
        body = f"""
        Hello, {name}!
        Congratulations on your achievement. You have completed the 5G Networks course. 

        Attached you will find your certificate. Please, verify that your data is correct. If anything is misspelled, reply to this email as quickly as possible for the necessary correction before sending it to the print shop. 

        All certificates will be printed and signed.
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Attach certificate
        cert_file = f'certificates/Certificate T123 (1)-{list(recipients.keys()).index(name) + 1}.pdf'
        with open(cert_file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

        try:
            # Send the email
            smtp.send_message(em)
            print(f"Email sent successfully to: {email_receiver}")
        except Exception as e:
            print(f"Failed to send email to {email_receiver}. Error: {e}")
