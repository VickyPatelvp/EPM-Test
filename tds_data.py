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

            total_salary = (users_ref.get().to_dict()["ctc"] * 12)

            # 80C (1,50,000 Limit)

            principle_home_loan = int(tds_data["Principal on Home loan"]["loanAmount"])

            primium_on_insurance = int(tds_data["Premium on Insurance"]["annualAmountofpolicy"])

            elss = int(tds_data["ELSS(SIP)"]["annualAmount"])

            annual_pf = float((users_ref.collection('salaryslips').document('sal001').get().to_dict())["epfo"]) * 12

            tution_fee = int(tds_data["Tution Fee"]["annualAmount"])

            total = principle_home_loan + primium_on_insurance + elss + annual_pf + tution_fee

            if total <= 150000:
                new_total_1 = total

            else:
                new_total_1 = 150000

            health_insurance = int(tds_data["Health Insurance (Self)"]["annualAmountofpolicy"]) + \
                               int(tds_data["Health Insurance (Spouse)"]["annualAmountofpolicy"]) + \
                               int(tds_data["Health Insurance (Father)"]["annualAmountofpolicy"])

            if health_insurance >= 50000:
                new_total_2 = 50000

            else:
                new_total_2 = health_insurance

            interest_on_home_loan = int(tds_data["Interest on Home Loan"]["annualInterestPayable/Paid"])

            if interest_on_home_loan >= 200000:
                new_total_3 = 200000

            else:
                new_total_3 = interest_on_home_loan

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

            # current_month = int(datetime.date.today().month)

            current_month = 7

            if current_month <= 3:
                no_of_remaining_month = 12 - 9 - current_month + 1
                tds_deducted_till_now = (int((users_ref.collection('salaryslips').document('sal001').get().to_dict())["tds"]) * (current_month - 1 + 9))
            else:
                no_of_remaining_month = 12 - 3 - current_month + 1
                tds_deducted_till_now = (int((users_ref.collection('salaryslips').document('sal001').get().to_dict())["tds"]) * (current_month - 1 - 3))

            if no_of_remaining_month == 0:
                tds = new_total_6
            else:
                tds = (new_total_6 - tds_deducted_till_now) / no_of_remaining_month

            print(int(tds))


TDSData.deduction(TDSData.deduction, id="EMP001")

