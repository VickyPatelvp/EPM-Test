import smtplib

class Mail():
  def __init__(self):
      pass

  def register_mail(self):
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
      subject = 'Company Registation Email'
      body = '''This mail is for Company Registration,
                you can register Your Company with As follow given link below
                http://192.168.0.150:3005/register
              warning: you have to specify your company name unique its very sensitive information
              it can not be chnage after you registered
      '''
      message = f"""
      From: {from_email}
      To: {to_email}
      Subject: {subject}
      {body}
      """
      # Send the email
      server.sendmail(from_email, to_email, message)
      # Close the SMTP connection
      server.quit()

  def register_responce_mail(self,companyname):
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
       subject = 'Yor Company Account'
       body = f'''This mail is for Company Successsfully registered,
                Now you can use following url to access your company login
                http://192.168.0.150:3005/{companyname}/login
              Congratulation, Thank you so much..'''
       message = f"""
        From: {from_email}
        To: {to_email}
        Subject: {subject}
        {body}
        """
        # Send the email
       server.sendmail(from_email, to_email, message)
        # Close the SMTP connection
       server.quit()

  def new_employee_mail(self,email,companyname):
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
      to_email = email
      subject = 'Employee Registation Form'
      body = '''This mail is for Registration,
                you can register with As follow given link below
                 http://192.168.0.150:3005/{companyname}/employee_regiter
                Thank You,
        '''

      message = f"""
        From: {from_email}
        To: {to_email}
        Subject: {subject}
        {body}
        """
      # Send the email
      server.sendmail(from_email, to_email, message)
      # Close the SMTP connection
      server.quit()


def employee_registered_mail(self, email,companyname):
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
    to_email = email
    subject = 'Employee Registation Successfull'
    body = f'''This mail is for Company Successsfully registered,
                Now you can use following url to access your company login
                http://192.168.0.150:3005/{companyname}/login
              Congratulation, Thank you so much..'''
    message = f"""
       From: {from_email}
       To: {to_email}
       Subject: {subject}
       {body}
       """
    # Send the email
    server.sendmail(from_email, to_email, message)
    # Close the SMTP connection
    server.quit()

def forgot_mail(self,uid,password,companyname,email):
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
    to_email = email
    subject = 'Forgot ID Password'
    body = f'''This mail is You request For Forgot password,
                Your,
                User ID: {uid}
                Password: {password}
                Now you can use following url to access your company login
                http://192.168.0.150:3005/{companyname}/login
              Congratulation, Thank you so much..'''
    message = f"""
       From: {from_email}
       To: {to_email}
       Subject: {subject}
       {body}
       """
    # Send the email
    server.sendmail(from_email, to_email, message)
    # Close the SMTP connection
    server.quit()







