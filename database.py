from firebase_admin import firestore
import firebase_admin

from firebase_admin import credentials
cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json')
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def result():

    ''' ADD FORM DETAILS INTO DATABASE '''

    name_list = ["Jay", "Meet", "Parth", "Jenil", "Gautam"]
    for num in range(0, 5):

        name = name_list[num]

        new_id = "EMP00" + str(num + 1)


        # ADD PERSONAL DATA

        personal_data = {
            'photo': 'photo',
            'employeeName': name, 'userID': new_id, 'department': 'Design',
            'email': f'{name}123@gmail.com',
            'ctc': 25000, 'jobPosition': 'junior',
            'manager': 'Design Manager', 'doj': '2023-04-03',
            'currentExperience':'3 year', 'dob': '1999-02-04', 'gender': 'male',
            'phoneNo': 35464531456,
            'bankName': 'BOB', 'accountHolderName': name,
            'accountNumber': '3561654653416541341',
            'ifscCode': 'BANKIFSC12',
            'aadharCardNo': 6546541654464, 'panCardNo': 'BNDJC4544D',
            'passportNo': 57847857878,
            'pfAccountNo': 'MABAN00000640000000125', 'uanNo': 100904319456, 'esicNo': 31001234560000001
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).set(personal_data)

        # ADD LEAVE DATA

        leave_data = {
        '2023-01-11': {'applydate': '2023-01-11', 'days': 1, 'fromdate': '2023-01-11', 'todate': '2023-01-12', 'type': 'SL'},
        'total_leaves': {'CL': 10, 'PL': 10, 'SL': 10, 'LWP': 0}
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("2023-01-11").set(leave_data["2023-01-11"])
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("total_leaves").set(leave_data["total_leaves"])
        leave_data = {
        '2023-02-25': {'applydate': '2023-02-20', 'days': 2, 'fromdate': '2023-02-25', 'todate': '2023-02-28', 'type': 'CL'},
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("2023-02-25").set(leave_data["2023-02-25"])
        # ADD SALARY DATA
        for i in range(1,13):
            salary_slip_data = {
                'employeeName': name, 'userID': new_id,'slip_id': 'sal001', 'lwp': 0, 'basic': 26500, 'da': 17225, 'hra': 2650, 'otherAllowance': 0,
                'incentive': 0, 'grsOutstandingAdjustment': 0, 'arrears': 0, 'statutoryBonus': 0,
                'grossSalary': 46375, 'epfo': 3180, 'dedOutstandingAdjustment': 0, 'pt': 200,
                'tds': 2650, 'otherDeduction': 0, 'leaveDeduction': 3533.33,'totalDeduction': 9563.33, 'netSalary': 36811.67 , 'month': 'January',
                'year': 2023,
            }
            db.collection(u'alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("sal00"+str(i)).set(salary_slip_data)
        # ADD TDS DATA

        tds_detail = {
            'hlapplicationno': 6548656,
            'hlamount': 20000,
            'hlperiod': '2 year',
            'hlname': name,
            'hlannual': '5%',
            'pino': 5454464,
            'piname': name,
            'piannual': 3545,
            'hipno': 466545,
            'hipname': name,
            'hipannual': 4545,
            'hipperiod': '2023 to 2024',
            'hisno': 6563,
            'hisname': 'XYZ',
            'hisannual': 2126,
            'hisperiod': '2023 to 2024',
            'hifno': 446556,
            'hifname': 'Father',
            'hifannual': 5464,
            'hifperiod': '2023 to 2024',
            'ihlannual': 2000,
            'ihlpanlender': 'JHHD56556',
            'ihlname': name,
            'ahrmonth': 2000,
            'ahrlandpann': 'NJHVJ6556S',
            'ahrperiod': '2023 to 2024',
            'ahrlandname': 'Ankit',
            'ahrlandaddress': 'Nadiad',
            'elssannual': 500,
            'elssperiod': '2023 to 2024',
            'tfannual': 1000,
            'tfperiod': '2023 to 2024'
        }




        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("tdsmst").document("tds").set(tds_detail)

result()