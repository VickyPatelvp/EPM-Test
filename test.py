# # # import os
# # #
# # # import firebase_admin
# # # from firebase_admin import credentials, storage
# # # from firebase_admin import credentials, storage
# # # from flask import Flask, render_template, request, redirect, url_for, flash, send_file
# # # from werkzeug.utils import secure_filename
# # # from base64 import b64encode
# # # import base64
# # # app = Flask(__name__)
# # #
# # # # Initialize Firebase app
# # # cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json')
# # # firebase_admin.initialize_app(cred, {
# # #     'storageBucket': 'employee-payroll-system-848cc.appspot.com'
# # # })
# # #
# # #
# # #
# # # # a= base64.b64encode
# # # @app.route('/', methods=['POST','GET'])
# # # def get_image():
# # #     # Get a reference to the image blob
# # #     if request.method=='POST':
# # #         FILE=request.files['file']
# # #         print(FILE.filename)
# # #         bucket = storage.bucket()
# # #         # blob = bucket.blob('1-5000x3333.jpg')
# # #         blob = bucket.get_blob('/images/Capture.PNG')
# # #
# # #
# # #         # Serve the image file
# # #         image_data = blob.download_as_bytes()
# # #         image_data=send_file(image_data, mimetype='image/jpeg')
# # #         # print(blob.public_url)
# # #
# # #     # Render the image in an HTML template
# # #         return render_template('upload.html', image_data=image_data)
# # #     return render_template('upload.html', image_data=None)
# # #
# # #
# # # @app.route('/images')
# # # def get_images():
# # #     # Get a reference to the image blob
# # #     bucket = storage.bucket()
# # #     blob = bucket.blob('/images/Capture.PNG')
# # #
# # #     # Serve the image file
# # #     return send_file(blob.download_as_bytes(), mimetype='image/jpeg')
# # #
# # #
# # # if __name__ == '__main__':
# # #     app.run(port=4000, debug=True)
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # import os
# # import urllib
# # from io import BytesIO
# #
# # import firebase_admin
# # from firebase_admin import credentials, storage
# # from firebase_admin import credentials, storage,initialize_app
# # from flask import Flask, render_template, request, redirect, url_for, flash, send_file
# # from werkzeug.utils import secure_filename
# # from base64 import b64encode
# # from PIL import Image
# # import base64
# # app = Flask(__name__)
# #
# # # firebaseConfig = {
# # #   "apiKey": "AIzaSyDrQdNtxLW6sWRDG-_wnrCW5hzu9oQUy0I",
# # #   "authDomain": "employee-payroll-system-848cc.firebaseapp.com",
# # #   "projectId": "employee-payroll-system-848cc",
# # #   "storageBucket": "employee-payroll-system-848cc.appspot.com",
# # #   "messagingSenderId": "99989108168",
# # #   "appId": "1:99989108168:web:65c1ccfb45178fc09bfcfd",
# # #   "serviceAccount":"empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json",
# # #     "databaseURL":"gs://employee-payroll-system-848cc.appspot.com"
# # # }
# #
# # # storage1=storage()
# # # firbase=firebase_admin.initialize_app(firebaseConfig)
# #
# #
# # cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json')
# # initialize_app(cred, {
# #     'storageBucket': 'employee-payroll-system-848cc.appspot.com'
# # })
# # app.config['images']='employee-payroll-system-848cc.appspot.com'
# # # a= base64.b64encode
# # @app.route('/', methods=['POST','GET'])
# # def upload_image():
# #     # Get a reference to the image blob
# #     if request.method=='POST':
# #         file = request.files['file']
# #         bucket = storage.bucket()
# #         blob = bucket.blob(f'empp001_{file.filename}')
# #         blob.upload_from_file(file)
# #         return redirect(url_for('get_image',filename=file.filename))
# #     return render_template('upload.html')
# #
# #
# # # @app.route('/image')
# # # def get_image():
# # #     # Retrieve image URL from Firebase Storage
# # #     bucket = storage.bucket()
# # #     blob = bucket.blob('Capture.PNG')
# # #     image_url = blob.generate_signed_url(expiration=600)  # URL expires in 10 minutes
# # #
# # #     # Render HTML template with image URL
# # #     return render_template('get_image.html', image_url=image_url)
# # #
# #
# #
# # @app.route('/image/<filename>')
# # def get_image(filename):
# #     # Retrieve image from Firebase Storage
# #     bucket = storage.bucket()
# #     blob = bucket.blob(filename)
# #     image_data = blob.download_as_bytes()
# #     # Convert image bytes to base64 encoded string
# #     image_b64 = base64.b64encode(image_data).decode('utf-8')
# #     # Create a PIL image object from the image data
# #     img = Image.open(BytesIO(image_data))
# #     # Get image dimensions
# #     width, height = img.size
# #     print(width,height)
# #     # Render HTML template with image data
# #     return render_template('get_image.html', image_data=image_b64, width=1600, height=1000)
# #
# #
# # if __name__ == '__main__':
# #     app.run(port=4000, debug=True)
# # import smtplib
# #
# #
# # def register_responce_mail():
# #     # Set up the connection to the SMTP server
# #     smtp_server = 'smtp.gmail.com'
# #     smtp_port = 587  # or 465 for SSL/TLS
# #     smtp_username = 'vickypatel.vp817@gmail.com'
# #     smtp_password = "qglshjrbjznxkepg"
# #     server = smtplib.SMTP(smtp_server, smtp_port)
# #     server.starttls()
# #     server.login(smtp_username, smtp_password)
# #     # Compose the email message
# #     from_email = 'vickypatel.vp817@gmail.com'
# #     to_email = 'vickypatel.vp817@gmail.com'
# #     subject = 'Yor Company Account'
# #     body = '''This mail is for Company Successsfully registered,
# #               Now you can use following url to access your company login
# #               http://192.168.0.150:3005/NV2/login
# #             Congratulation, Thank you so much..'''
# #     message = f"""
# #       From: {from_email}
# #       To: {to_email}
# #       Subject: {subject}
# #       {body}
# #       """
# #     # Send the email
# #     server.sendmail(from_email, to_email, message)
# #     # Close the SMTP connection
# #     server.quit()
# #
# #
# #
# # register_responce_mail()
# import datetime
# start = datetime.datetime.now()

# from firebase_admin import firestore
# import firebase_admin

# from firebase_admin import credentials


# print(start)

# cred = credentials.Certificate('fir-emp-7d1ed-firebase-adminsdk-kzxuw-f9465d22f8.json')

# firebase_app = firebase_admin.initialize_app(cred)

# db = firestore.client()

# estart = datetime.datetime.now()

# print(estart-start)


# # start = datetime.datetime.now()

# # for num in range(0, 100):
# #
# #     # admin_data = {
# #     #     'AdminID': 'admin@aliansoftware.com',
# #     #     'Company Name': 'alian',
# #     #     'password': 12345
# #     # }
# #     #
# #     # db.collection('alian').document(u'admin').collection('employee').document('num').collection('emp').document('demo'+str(num)).set(admin_data)
# #     # # ADD DEPARTMENT DATA
# #     # db.collection('demo').document('demo'+str(num)).set(admin_data)
# #     # print(num)
# #     dict_data={}
# #     data=db.collection('alian').document(u'admin').collection('employee').document('num').collection('emp').document(
# #         'demo' + str(num)).get()
# #     db.collection('demo').document('demo' + str(num)).set(admin_data)
# #     dict.update({num :data})
# #
# # endtime=datetime.datetime.now()
# #
# # print(start-endtime)

# # dict_data = {}
# #
# # start = datetime.datetime.now()
# # for num in range(0, 100):
# #     admin_data = {
# #         'AdminID': 'admin@aliansoftware.com',
# #         'Company Name': 'alian',
# #         'password': 12345
# #     }
# #     dict_data.update({str(num): admin_data})
# # db.collection('alian').document(u'admin').collection('employee').document('num').collection('emp').document('demohello').set(dict_data)
# # endtime=datetime.datetime.now()
# #
# # print(endtime- start)
# #
# #
# #
# #
# #
# #     # ADD DEPARTMENT DATA
# #
# # dict_data = {}
# # start = datetime.datetime.now()
# # for num in range(0, 100):
# #     admin_data = {
# #         'AdminID': 'admin@aliansoftware.com',
# #         'Company Name': 'alian',
# #         'password': 12345
# #     }
# #     dict_data.update({str(num): admin_data})
# #
# # db.collection('demo').document('demo'+str(num)).set(dict_data)
# #
# # endtime=datetime.datetime.now()
# #
# # print(endtime-start)


# start = datetime.datetime.now()

# db.collection('alian').document(u'admin').collection('employee').document('num').collection('emp').document('demohello').get()


# endtime=datetime.datetime.now()

# print(endtime-start)


# start = datetime.datetime.now()
# db.collection('demo').document('demo99').get()
# endtime=datetime.datetime.now()
# print(endtime-start)





# # start = datetime.datetime.now()
# # dict_data = {}
# # for num in range(0, 10):
# #     data=db.collection('demo').document('demo' + str(num)).get()
# #     dict.update({num :data})
# #
# # endtime=datetime.datetime.now()
# # print(endtime-start)
# #
# # start = datetime.datetime.now()
# # dict_data = {}
# # for num in range(0, 10):
# #     data=db.collection('alian').document(u'admin').collection('employee').document('num').collection('emp').document(
# #         'demo' + str(num)).get()
# #     dict.update({num :data})
# # endtime=datetime.datetime.now()
# # print(endtime-start)



# import calendar
# import datetime
#
# # Define US Federal holidays
# us_holidays = {
#     datetime.date(2023, 1, 1),  # New Year's Day
#     datetime.date(2023, 1, 16), # Martin Luther King Jr. Day
#     datetime.date(2023, 2, 20), # Presidents' Day
#     datetime.date(2023, 5, 29), # Memorial Day
#     datetime.date(2023, 7, 4),  # Independence Day
#     datetime.date(2023, 9, 4),  # Labor Day
#     datetime.date(2023, 10, 9), # Columbus Day
#     datetime.date(2023, 11, 10),# Veterans Day
#     datetime.date(2023, 11, 23),# Thanksgiving Day
#     datetime.date(2023, 12, 25),# Christmas Day
# }
#
# # Create a list of holidays month-wise
# holidays_monthwise = {}
# for month in range(1, 13):
#     # Get the number of days in the current month
#     num_days = calendar.monthrange(2023, month)[1]
#
#     # Initialize an empty list for holidays in the current month
#     month_holidays = []
#
#     # Iterate over the days in the current month and add any holidays to the list
#     for day in range(1, num_days+1):
#         date = datetime.date(2023, month, day)
#         if date in us_holidays:
#             month_holidays.append(date.strftime("%Y-%m-%d"))
#
#     # Add the list of holidays for the current month to the dictionary
#     holidays_monthwise[month] = month_holidays
#
# # Print the list of holidays month-wise
# for month, holidays in holidays_monthwise.items():
#     print(f"Holidays for month {month}:")
#     print(holidays)


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initialize the Firebase Admin SDK
cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json')
firebase_admin.initialize_app(cred)

# access the Firestore database and collection
db = firestore.client()
# collection_ref = db.collection("VV").document("employee").collection('employee').where('email', "==", 'vivekpatel.vp817@gmail.com' ).where('password',"==",'1').get()
docs=db.collection('alian_software').document(u'employee').collection('employee').get()

# print(len(collection_ref))
# if len(collection_ref) > 0:
#     document = collection_ref[0].to_dict()
#     print(document)

# print the document

print(docs[-1].to_dict()['userID'])



