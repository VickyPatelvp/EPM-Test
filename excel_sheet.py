import openpyxl
import calendar
from salary_manage import Salarymanage
import os


class SalaryData():

    def __init__(self,db):
        self.db=db

    def add_data(self, salid):
        mont_in_num = int(salid[5:])
        month = calendar.month_name[mont_in_num]

        # Create a new workbook
        workbook = openpyxl.Workbook()

        # Store Excelsheet
        file_path = f"C:/Users/alian/Desktop/EPM-Test/Excelsheets/"

        if not os.path.exists(file_path):
            os.makedirs(file_path)

        file_name = f'Salary_{month}.xlsx'

        excel_file = file_path + file_name

        # Select the active worksheet
        worksheet = workbook.active

        # Worksheet Name
        worksheet.title = "Alian Software"

        # Merge cell for heading
        A1 = worksheet.merge_cells('A1:Z1')

        # Heading
        worksheet['A1'] = 'Bank Name Associated With Company'

        # Set Table Header
        title_row = ["Employee Name", "Bank Name", "Account No", "IFSC Code", "Total Salary"]
        worksheet.append(title_row)

        workbook.save(excel_file)

        salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid)
        for i in salary_list:

            empid = salary_list[i]["userID"]

            user_ref = self.db.collection(u'alian_software').document('employee').collection('employee').document(empid)

            data = user_ref.get().to_dict()

            salary_data = user_ref.collection("salaryslips").document(f"{salid}").get().to_dict()

            name = data["accountHolderName"]

            bank_name = data["bankName"]

            account_number = data["accountNumber"]

            ifsc_code = data["ifscCode"]

            total_salary = salary_data["netSalary"]

            employee_data = [name, bank_name, account_number, ifsc_code, total_salary]
            
            worksheet.append(employee_data)

            # Save the workbook
            workbook.save(excel_file)

