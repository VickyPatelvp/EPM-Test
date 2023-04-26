from flask import request

from firebase_admin import firestore, storage

db = firestore.client()


def result():

    ''' ADD FORM DETAILS INTO DATABASE '''

    new_id = str(int(len(db.collection(u'alian_software').document(u'employee').collection('employee').get())) + 1)
    if request.method == 'POST':
        file = request.files['file']
        image_name=f'{new_id}_{file.filename}'
        bucket = storage.bucket()
        blob = bucket.blob(image_name)
        blob.upload_from_file(file)

        # Get a reference to the image blob
        # ADD PERSONAL DATA

        personal_data = {
            'photo': request.form.get(image_name),
            'employeeName': request.form.get('name'), 'userID': new_id, 'department': request.form.get('department'),
            'email': request.form.get('email'),
            'ctc': request.form.get('ctc'), 'jobPosition': request.form.get('jobposition'),
            'manager': request.form.get('manager'), 'doj': request.form.get('doj'),
            'currentExperience': request.form.get('currentExperience'), 'dob': request.form.get('dob'), 'gender': request.form.get('gender'),
            'phoneNo': request.form.get('mobileno'),
            'bankName': request.form.get('bankname'), 'accountHolderName': request.form.get('accountholdername'),
            'accountNumber': request.form.get('accountno'), 'ifscCode': request.form.get('ifsccode'),
            'aadharCardNo': request.form.get('aadharno'), 'panCardNo': request.form.get('panno'),
            'passportNo': request.form.get('passportno'),
            'pfAccountNo': 'MABAN00000640000000125', 'uanNo': '100904319456', 'esicNo': '31–00–123456–000–0001'
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).set(personal_data)

        # ADD LEAVE DATA

        leave_data = {

            'total_leaves': {'CL': 10, 'PL': 10, 'SL': 10, 'LWP': 0}
        }

        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("leaveMST").document("total_leaves").set(leave_data["total_leaves"])

        # ADD SALARY DATA
        salary_slip_data = {
            'employeeName': request.form.get('name'), 'userID': new_id, 'slip_id': '', 'lwp': "", 'basic': "", 'da': "", 'hra': "", 'otherAllowance': "",
            'incentive': "", 'outstandingAdjustment': "", 'arrears': "", 'statutoryBonus': '',
            'grossSalary': "", 'epfo': "", 'outstandingAdjustments': "", 'pt': "",
            'tds': "", 'otherDeduction': "", 'leaveDeduction': "",'totalDeduction': "", 'netSalary': ""
        }
        db.collection('alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("slipid").set(salary_slip_data)

        # salary_slip_data = {
        #     'employeeName': request.form.get('name'), 'userID': new_id,'slip_id': '', 'lwp': "", 'basic': "", 'da': "", 'hra': "", 'otherAllowance': "",
        #     'incentive': "", 'grsOutstandingAdjustment': "", 'arrears': "", 'statutoryBonus': '',
        #     'grossSalary': "", 'epfo': "", 'dedOutstandingAdjustment': "", 'pt': "",
        #     'tds': "", 'otherDeduction': "", 'leaveDeduction': "",'totalDeduction': "", 'netSalary': "",'month':'','year':''
        # }
        # db.collection(u'alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("slipid").set(salary_slip_data)


        # ADD TDS DATA

        tds_detail = {
                'hlapplicationno': request.form.get('hlapplicationno'),
                'hlamount': request.form.get('hlamount'),
                'hlperiod': request.form.get('hlperiod'),
                'hlname': request.form.get('hlname'),
                'hlannual': request.form.get('hlannual'),
                'pino': request.form.get('pino'),
                'piname': request.form.get('piname'),
                'piannual': request.form.get('piannual'),
                'hipno': request.form.get('hipno'),
                'hipname': request.form.get('hipname'),
                'hipannual': request.form.get('hipannual'),
                'hipperiod': request.form.get('hipperiod'),
                'hisno': request.form.get('hisno'),
                'hisname': request.form.get('hisname'),
                'hisannual': request.form.get('hisannual'),
                'hisperiod': request.form.get('hisperiod'),
                'hifno': request.form.get('hifno'),
                'hifname': request.form.get('hifname'),
                'hifannual': request.form.get('hifannual'),
                'hifperiod': request.form.get('hifperiod'),
                'ihlannual': request.form.get('ihlannual'),
                'ihlpanlender': request.form.get('ihlpanlender'),
                'ihlname': request.form.get("ihlname"),
                'ahrmonth': request.form.get("ahrmonth"),
                'ahrlandpann': request.form.get("ahrlandpann"),
                'ahrperiod': request.form.get("ahrperiod"),
                'ahrlandname': request.form.get("ahrlandname"),
                'ahrlandaddress': request.form.get("ahrlandaddress"),
                'elssannual': request.form.get("elssannual"),
                'elssperiod': request.form.get("elssperiod"),
                'tfannual': request.form.get("tfannual"),
                'tfperiod': request.form.get("tfperiod")
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("tdsmst").document("tds").set(tds_detail)
