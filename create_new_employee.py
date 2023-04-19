from flask import request

from firebase_admin import firestore


db = firestore.client()


def result():

    ''' ADD FORM DETAILS INTO DATABASE '''

    new_id = str(int(len(db.collection(u'alian_software').document(u'employee').collection('employee').get())) + 1)
    if request.method == 'POST':

        # ADD PERSONAL DATA

        personal_data = {
            'photo': request.form.get('photo'),
            'employeeName': request.form.get('name'), 'userID': new_id, 'department': request.form.get('department'),
            'email': request.form.get('email'),
            'ctc': request.form.get('ctc'), 'jobPosition': request.form.get('jobposition'),
            'manager': request.form.get('manager'), 'doj': request.form.get('doj'),
            'currentExperience': request.form.get('currentExperience'), 'dob': request.form.get('dob'), 'gender': request.form.get('gender'),
            'phoneNo': request.form.get('mobileno'),
            'bankName': request.form.get('bankname'), 'accountHolderName': request.form.get('accountholdername'),
            'accountNumber': request.form.get('accountno'),
            'aadharCardNo': request.form.get('aadharno'), 'panCardNo': request.form.get('panno'),
            'passportNo': request.form.get('passportno'),
            'pfAccountNo': 'MABAN00000640000000125', 'uanNo': '100904319456', 'esicNo': '31–00–123456–000–0001'
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).set(personal_data)

        # ADD LEAVE DATA

        leave_data = {
            'date': {'num_of_day': '', 'sdate': '', 'type': ''},
            'total_leaves': {'CL': '', 'PL': '', 'SL': ''}
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("leaveMST").document("date").set(leave_data["date"])
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("leaveMST").document("total_leaves").set(leave_data["total_leaves"])

        # ADD SALARY DATA

        salary_slip_data = {
            'slip_id': '', 'lwp': "", 'basic': "", 'da': "", 'hra': "", 'otherAllowance': "",
            'incentive': "", 'outstandingAdjustment': "", 'arrears': "", 'statutoryBonus': '',
            'grossSalary': "", 'epfo': "", 'outstandingAdjustments': "", 'pt': "",
            'tds': "", 'otherDeduction': "", 'leaveDeduction': "",'totalDeduction': "", 'netSalary': ""
        }
        db.collection(u'alian_software').document('employee').collection('employee').document(new_id).collection('salaryslips').document("slipid").set(salary_slip_data)

        # ADD TDS DATA

        tds_detail = {
            'Principal on Home loan': {
                'applicationNo': request.form.get('hlapplicationno'),
                'loanAmount': request.form.get('hlamount'),
                'PeriodofHomeLoan': request.form.get('hlperiod'),
                'nameofPerson': request.form.get('hlname'),
                'annualInterest': request.form.get('hlannual')
            },
            'Premium on Insurance': {
                'insuranceNo': request.form.get('pino'),
                'nameofInsured': request.form.get('piname'),
                'annualAmountofpolicy': request.form.get('piannual')
            },
            'Health Insurance (Self)': {
                'insuranceNo': request.form.get('hipno'),
                'nameofInsured': request.form.get('hipname'),
                'annualAmountofpolicy': request.form.get('hipannual'),
                'periodofInsurance': request.form.get('hipperiod')
            },
            'Health Insurance (Spouse)': {
                'insuranceNo': request.form.get('hisno'),
                'nameofInsured': request.form.get('hisname'),
                'annualAmountofpolicy': request.form.get('hisannual'),
                'periodofInsurance': request.form.get('hisperiod')
            },
            'Health Insurance (Father)': {
                'insuranceNo': request.form.get('hifno'),
                'nameofInsured': request.form.get('hifname'),
                'annualAmountofpolicy': request.form.get('hifannual'),
                'periodofInsurance': request.form.get('hifperiod')
            },
            'Interest on Home Loan': {
                'annualInterestPayable/Paid': request.form.get('ihlannual'),
                'panofLender': request.form.get('ihlpanlender'),
                'nameofPerson': request.form.get("ihlname")
            },
            'Annual House Rent': {
                'currentMonthRent': request.form.get("ahrmonth"),
                'lenderPAN': request.form.get("ahrlandpann"),
                'periodofDate': request.form.get("ahrperiod"),
                'nameofLandloard': request.form.get("ahrlandname"),
                'landloardAddress': request.form.get("ahrlandaddress")
            },
            'ELSS(SIP)': {
                'annualAmount': request.form.get("elssannual"),
                'periodofDate': request.form.get("elssperiod")
            },
            'Tution Fee': {
                'annualAmount': request.form.get("tfannual"),
                'periodofDate': request.form.get("tfperiod")
            }
        }
        db.collection(u'alian_software').document(u'employee').collection('employee').document(new_id).collection("tdsmst").document("tds").set(tds_detail)
