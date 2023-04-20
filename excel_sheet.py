import openpyxl
import datetime

# from firebase_admin import firestore
# import firebase_admin

# from firebase_admin import credentials
# cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
# firebase_app = firebase_admin.initialize_app(cred)

# db = firestore.client()


# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

# Worksheet Name
worksheet.title = "Company Name"

# Merge cell for heading
A1 = worksheet.merge_cells('A1:Z1')

# Heading 
worksheet['A1'] = 'Bank Name Associated With Company'

# Set Table Header
title_row = ["Employee Name", "Bank Name", "Account No","IFSC Code", "Total Salary"]
worksheet.append(title_row)

workbook.save('bank.xlsx')


class SalaryData():

    def __init__(self,db):
        self.db=db

    
    def add_data(self, id):

        if datetime.date.today().day==20:

            # current_month = datetime.date.today().month

            current_month = 2

            user_ref = self.db.collection(u'alian_software').document('employee').collection('employee').document(id)

            data = user_ref.get().to_dict()

            salary_data = user_ref.collection("salaryslips").document(f"sal00{current_month - 1}").get().to_dict()

            name = data["accountHolderName"]

            bank_name = data["bankName"]

            account_number = data["accountNumber"]

            ifsc_code = data["ifscCode"]

            total_salary = salary_data["netSalary"]

            employee_data = [name, bank_name, account_number, ifsc_code, total_salary]
            
            worksheet.append(employee_data)

            # Save the workbook
            workbook.save('bank.xlsx')




# SalaryData.create_sheet(SalaryData.create_sheet)

# SalaryData.add_data(SalaryData.add_data, "EMP002")
# SalaryData.add_data(SalaryData.add_data, "EMP002")
# SalaryData.add_data(SalaryData.add_data, "EMP002")
