import datetime
import calendar
from email.mime.application import MIMEApplication

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


class Mail():
    def __init__(self):
        pass

    def register_mail(self,email):
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
        to_email = email

        body = '''This mail is for Company Registration,
                you can register Your Company with As follow given link below
                http://127.0.0.1:300/
              warning: you have to specify your company name unique its very sensitive information
              it can not be chnage after you registered
         '''
        message = f"Subject: {subject}\n\n{body}"
        # Send the email
        server.sendmail(from_email, to_email, message)
        # Close the SMTP connection
        server.quit()

    def register_responce_mail(self, companyname,email):
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
        to_email = email
        subject = 'Yor Company Account'
        body = f'''This mail is for Company Successsfully registered,
                Now you can use following url to access your company login
                this link is for new company register and insert data you have to open this link first 
                http://127.0.0.1:300/{companyname}/Admin/add_data
                \n\n
                once you have added company data then use this link:
                http://127.0.0.1:300/{companyname}/login
              Congratulation, Thank you so much..'''
        message = f"Subject: {subject}\n\n{body}"
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

        message = f"Subject: {subject}\n\n{body}"
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
        body = f'''This mail is for Employee Successsfully registered,
                Now you can use following url to access your company login
               http://127.0.0.1:300/{companyname}/login
              Congratulation, Thank you so much..'''
        message = f"Subject: {subject}\n\n{body}"
        # Send the email
        server.sendmail(from_email, to_email, message)
        # Close the SMTP connection
        server.quit()
    def forgot_mail(self,email, password, companyname, company_mail,auth_password):
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
                    User ID: {email}
                    Password: {password}
                    Now you can use following url to access your company login
                    http://127.0.0.1:300/{companyname}/login
                  Congratulation, Thank you so much..'''
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail(from_email, to_email, message)
        # Close the SMTP connection
        server.quit()

    def send_employee_pdf(self, data,path, company_mail,auth_password):
        # Set up the connection to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # or 587 for SSL/TLS
        if "@gmail.com" in company_mail:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587  # or 587 for SSL/TLS
        elif "@yahoo.com" in company_mail:
            smtp_server = 'smtp.mail.yahoo.com'
            smtp_port = 587  # or 587 for SSL/TLS
        # sending as mail


        # sending as mail
        MY_EMAIL = company_mail
        MY_PASSWORD = auth_password
        TO_EMAIL = data['email']
        current_month = int(datetime.datetime.today().month)

        if current_month == 1:
            current_month = 13
        else:
            current_month = current_month

        month_name = calendar.month_name[current_month - 1]

        empid = data['userID']
        salid = 'sal00' + str(current_month - 1)

        pdfname = f'{path}/Salaryslips/{month_name}/{empid}_{salid}.pdf'

        # Create a multipart message and set headers
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = MY_EMAIL
        message['To'] = MY_PASSWORD
        message['Subject'] = 'This email has an attachment, a pdf file'

        # message in mail
        body = '''Dear Employee,

               This is computer generated slip
               In case of any concern please
               connect with HR department.'''

        # Open PDF file in binary mode
        with open(pdfname, "rb") as attachment:
            # Add file as application/octet-stream
            # Email clients can usually download this automatically as attachment
            pdf_part = MIMEApplication(attachment.read(), _subtype="pdf")
            pdf_part.add_header('Content-Disposition', 'attachment', filename=pdfname)
            message.attach(pdf_part)
        # Convert message to string
        text = message.as_string()

        # Login to SMTP server and send email
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(MY_EMAIL, TO_EMAIL, text)

        print("Email sent successfully")


