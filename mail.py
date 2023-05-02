import smtplib


class Mail():
    def __init__(self):
        pass

    def register_mail(self):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.mail.yahoo.com'
        smtp_port = 587   # or 587 for SSL/TLS
        smtp_username = 'vick.patel887@yahoo.com'
        smtp_password = "lamarknnonluyqje"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email message
        subject = 'Company Registation Email'
        from_email = 'vick.patel887@yahoo.com'
        to_email = 'vickypatelvp870@gmail.com'

        body = '''This mail is for Company Registration,
                you can register Your Company with As follow given link below
                http://127.0.0.1:300/
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

    def register_responce_mail(self, companyname):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.mail.yahoo.com'
        smtp_port = 587  # or 587 for SSL/TLS
        smtp_username = 'vick.patel887@yahoo.com'
        smtp_password = "lamarknnonluyqje"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email message
        from_email = 'vick.patel887@yahoo.com'
        to_email = 'vickypatelvp870@gmail.com'
        subject = 'Yor Company Account'
        body = f'''This mail is for Company Successsfully registered,
                Now you can use following url to access your company login
                http://127.0.0.1:300/{companyname}/login
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

    def new_employee_mail(self, email, companyname ,company_mail,auth_password ):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # or 587 for SSL/TLS
        if "@gmail.com" in company_mail:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # or 587 for SSL/TLS
        elif "@yahoo.com" in company_mail:
            smtp_server = 'smtp.mail.yahoo.com'
            smtp_port = 587  # or 587 for SSL/TLS
        smtp_username = company_mail
        smtp_password = auth_password

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email message
        from_email = company_mail

        to_email = email
        subject = 'Employee Registation Form'
        body = f'''This mail is for Registration,
                you can register with As follow given link below
                 http://127.0.0.1:300/{companyname}/register_employee
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

    def employee_registered_mail(self, email, companyname ,company_mail,auth_password ):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # or 587 for SSL/TLS
        if "@gmail.com" in company_mail:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # or 587 for SSL/TLS
        elif "@yahoo.com" in company_mail:
            smtp_server = 'smtp.mail.yahoo.com'
            smtp_port = 587  # or 587 for SSL/TLS
        smtp_username = company_mail
        smtp_password =auth_password

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email message
        from_email = company_mail
        to_email = email
        subject = 'Employee Registation Successfull'
        body = f'''This mail is for Company Successsfully registered,
                Now you can use following url to access your company login
               http://127.0.0.1:300/{companyname}/login
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
    def forgot_mail(self, uid, password, companyname, email, company_mail,auth_password):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # or 587 for SSL/TLS
        if "@gmail.com" in company_mail:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # or 587 for SSL/TLS
        elif "@yahoo.com" in company_mail:
            smtp_server = 'smtp.mail.yahoo.com'
            smtp_port = 587  # or 587 for SSL/TLS
        smtp_username = company_mail
        smtp_password = auth_password

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        # Compose the email message
        from_email = 'vick.patel887@yahoo.com'
        to_email = email
        subject = 'Forgot ID Password'
        body = f'''This mail is You request For Forgot password,
                    Your,
                    User ID: {uid}
                    Password: {password}
                    Now you can use following url to access your company login
                    http://127.0.0.1:300/{companyname}/login
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


