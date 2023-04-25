import smtplib

# Set up the connection to the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # or 465 for SSL/TLS
smtp_username = 'vickypatel.vp817@gmail.com'
smtp_password = "qglshjrbjznxkepg"

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Compose the email message
from_email = 'vickypatel.vp817@gmail.com'
to_email = 'vickypatel.vp817@gmail.com'
subject = 'Test Email'
body = '''This mail is for Company Registration,
          you can register Your Company with As follow given link below
          http://192.168.0.150:3005/register
        warning: you have to specify your company name unique its very sensitive information
'''
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