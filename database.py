from firebase_admin import firestore
import firebase_admin

from firebase_admin import credentials
cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
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
            'accountNumber': 3561654653416541341,
            'aadharCardNo': 6546541654464, 'panCardNo': 'BNDJC4544D',
            'passportNo': 57847857878,
            'pfAccountNo': 'MABAN00000640000000125', 'uanNo': 100904319456, 'esicNo': 31001234560000001
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).set(personal_data)

        # ADD LEAVE DATA

        leave_data = {
        '11-01-2023': {'applydate': '2023-01-11', 'days': 1, 'fromdate': '2023-01-11', 'todate': '2023-01-12', 'type': 'SL'},
        'total_leaves': {'CL': 10, 'PL': 10, 'SL': 10, 'LWP': 0}
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("11-01-2023").set(leave_data["11-01-2023"])
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("total_leaves").set(leave_data["total_leaves"])
        leave_data = {
        '25-02-2023': {'applydate': '2023-02-20', 'days': 2, 'fromdate': '2023-02-25', 'todate': '2023-02-28', 'type': 'CL'},
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection(
            "leaveMST").document("25-02-2023").set(leave_data["25-02-2023"])


        # ADD SALARY DATA

        salary_slip_data = {
            'slip_id': 'sal001', 'lwp': 0, 'basic': 26500, 'da': 17225, 'hra': 2650, 'otherAllowance': 0,
            'incentive': 0, 'grsOutstandingAdjustment': 0, 'arrears': 0, 'statutoryBonus': 0,
            'grossSalary': 46375, 'epfo': 3180, 'dedOutstandingAdjustment': 0, 'pt': 200,
            'tds': 2650, 'otherDeduction': 0, 'leaveDeduction': 3533.33,'totalDeduction': 9563.33, 'netSalary': 36811.67 , 'month': 'January',
            'year': 2023
        }
        db.collection(u'alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("sal001").set(salary_slip_data)
        salary_slip_data_two = {
            'slip_id': 'sal002', 'lwp': 0, 'basic': 26500, 'da': 17225, 'hra': 2650, 'otherAllowance': 0,
            'incentive': 0, 'grsOutstandingAdjustment': 0, 'arrears': 0, 'statutoryBonus': 0,
            'grossSalary': 46375, 'epfo': 3180, 'dedOutstandingAdjustment': 0, 'pt': 200,
            'tds': 2650, 'otherDeduction': 0, 'leaveDeduction': 3533.33,'totalDeduction': 9563.33, 'netSalary': 36811.67, 'month': 'Feb',  'year': 2023
        }
        db.collection(u'alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("sal002").set(salary_slip_data_two)

        # ADD TDS DATA

        tds_detail = {
            'Principal on Home loan': {
                'applicationNo': 6548656,
                'loanAmount': 20000,
                'PeriodofHomeLoan': '2 years',
                'nameofPerson': name,
                'annualInterest': '5%'
            },
            'Premium on Insurance': {
                'insuranceNo': 545154565,
                'nameofInsured': name,
                'annualAmountofpolicy': 3545
            },
            'Health Insurance (Self)': {
                'insuranceNo': 6566624,
                'nameofInsured': name,
                'annualAmountofpolicy': 3544,
                'periodofInsurance': '2023 to 2024'
            },
            'Health Insurance (Spouse)': {
                'insuranceNo': 3416565,
                'nameofInsured': 'Xyz',
                'annualAmountofpolicy': 2126,
                'periodofInsurance': '2023 to 2024'
            },
            'Health Insurance (Father)': {
                'insuranceNo': 6574846,
                'nameofInsured': 'P',
                'annualAmountofpolicy': 2120,
                'periodofInsurance': '2023 to 2024'
            },
            'Interest on Home Loan': {
                'annualInterestPayable/Paid': 2000,
                'panofLender': 'NHADN5655D',
                'nameofPerson': name
            },
            'Annual House Rent': {
                'currentMonthRent': 2000,
                'lenderPAN': 'AFAFF55554D',
                'periodofDate': '2023 to 2024',
                'nameofLandloard': 'Ankit',
                'landloardAddress': 'Nadiad'
            },
            'ELSS(SIP)': {
                'annualAmount': 500,
                'periodofDate': '2023 to 2024'
            },
            'Tution Fee': {
                'annualAmount': 1000,
                'periodofDate': '2023 to 2024'
            }
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("tdsmst").document("tds").set(tds_detail)

result()