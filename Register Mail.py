import smtplib

# Set up the connection to the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # or 465 for SSL/TLS
smtp_username = 'vickypatel.vp817@gmail.com'
smtp_password = 'vicky@aworld9902'

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Compose the email message
from_email = 'vickypatel.vp817@gmail.com'
to_email = 'vickypatel.vp817@gmail.com'
subject = 'Test Email'
body = 'Hello, this is a test email sent via SMTP.'

message = f"""\
From: {from_email}
To: {to_email}
Subject: {subject}

{body}
"""

# Send the email
server.sendmail(from_email, to_email, message)

# Close the SMTP connection
server.quit()