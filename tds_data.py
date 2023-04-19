from firebase_admin import firestore
import firebase_admin

from firebase_admin import credentials
cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()

import datetime


class TDSData():

    def __init__(self, db):
        self.db = db

    def deduction(self, id):

        ''' Calculate TDS '''

        if datetime.date.today().day == 19:

            users_ref = db.collection(u'alian_software').document('employee').collection('employee').document(id)

            tds_data = users_ref.collection('tdsmst').document('tds').get().to_dict()

            # print(tds_data)

            # current_month = int(datetime.date.today().month)

            current_month = 7

            # Annual Salary of Employee

            total_salary = int(users_ref.get().to_dict()["ctc"] * 12)

            # TDS Data from Database

            principle_home_loan = int(tds_data["Principal on Home loan"]["loanAmount"])

            primium_on_insurance = int(tds_data["Premium on Insurance"]["annualAmountofpolicy"])

            elss = int(tds_data["ELSS(SIP)"]["annualAmount"])

            tution_fee = int(tds_data["Tution Fee"]["annualAmount"])

            # EPFO Data from previous Salaryslip

            if current_month == 1:
                annual_pf = int((users_ref.collection('salaryslips').document(f'sal00{12-current_month}').get().to_dict())["epfo"]) * 12
            elif current_month == 2:
                annual_pf = int((users_ref.collection('salaryslips').document(f'sal00{13-current_month}').get().to_dict())["epfo"]) * 12
            else:
                annual_pf = int((users_ref.collection('salaryslips').document(f'sal00{current_month-2}').get().to_dict())["epfo"]) * 12

            # 80C (1,50,000 Limit)

            total = principle_home_loan + primium_on_insurance + elss + annual_pf + tution_fee

            if total <= 150000:
                new_total_1 = total

            else:
                new_total_1 = 150000

            # TDS Health Insurance 

            health_insurance = int(tds_data["Health Insurance (Self)"]["annualAmountofpolicy"]) + \
                               int(tds_data["Health Insurance (Spouse)"]["annualAmountofpolicy"]) + \
                               int(tds_data["Health Insurance (Father)"]["annualAmountofpolicy"])

            if health_insurance >= 50000:
                new_total_2 = 50000

            else:
                new_total_2 = health_insurance

            # TDS Interest on Home loan

            interest_on_home_loan = int(tds_data["Interest on Home Loan"]["annualInterestPayable/Paid"])

            if interest_on_home_loan >= 200000:
                new_total_3 = 200000

            else:
                new_total_3 = interest_on_home_loan

            # TDS House rent

            annual_house_rent = int(tds_data["Annual House Rent"]["currentMonthRent"]) * 12

            if principle_home_loan > 0:
                new_total_4 = 0
            else:
                min_annual_house_rent = min(
                    (annual_house_rent - (((total_salary - new_total_1 - new_total_2 - new_total_3)) * 0.1)),
                    (total_salary * 0.25), 60000)
                if min_annual_house_rent < 0:
                    new_total_4 = 0
                else:
                    new_total_4 = min_annual_house_rent

            gross_salary_taxable = total_salary - new_total_1 - new_total_2 - new_total_3 - new_total_4 - 50000

            if gross_salary_taxable > 1000000:
                new_total_5 = ((gross_salary_taxable - 1000000) * 0.3 + (500000 * 0.2) + 12500)

            elif gross_salary_taxable > 500000:
                new_total_5 = ((gross_salary_taxable - 500000) * 0.2 + 12500)

            else:
                new_total_5 = 0

            education_cess = new_total_5 * 0.04

            if (new_total_5 + education_cess) > 0:
                new_total_6 = new_total_5 + education_cess
            else:
                new_total_6 = 0

            # Previous Month TDS and remaining Months

            if current_month <= 4:
                no_of_remaining_month = (12 - 9 - current_month) + 2
                if current_month <= 2: 
                    tds_deducted_till_now = (int((users_ref.collection('salaryslips').document(f'sal00{str(10 + current_month)}').get().to_dict())["tds"])) * (no_of_remaining_month)
                else:
                    tds_deducted_till_now = (int((users_ref.collection('salaryslips').document(f'sal00{str(current_month - 2)}').get().to_dict())["tds"]) * (no_of_remaining_month))
            elif current_month == 5:
                no_of_remaining_month = 12
                tds_deducted_till_now = 0
            else:
                no_of_remaining_month = (12 - current_month) + 5
                tds_deducted_till_now = (int((users_ref.collection('salaryslips').document(f'sal00{str(current_month - 2)}').get().to_dict())["tds"]) * (no_of_remaining_month))

            # TDS Calculate 

            if no_of_remaining_month == 0:
                tds = abs(new_total_6)
            else:
                tds = abs((new_total_6 - tds_deducted_till_now) / no_of_remaining_month)

            # Store TDS deduction to database
                
            if current_month == 1:
                users_ref.collection('salaryslips').document(f'sal00{str(13 - current_month)}').update({"tds":tds})
            else:
                users_ref.collection('salaryslips').document(f'sal00{str(current_month - 1)}').update({"tds":tds})


TDSData.deduction(TDSData.deduction, id="EMP002")

