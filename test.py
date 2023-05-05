# import openpyxl
# import datetime
# import re
# class ExcelData():
#     def __init__(self, db):
#         self.db = db
#     def store_excel_data(self, companyname, path):
#         # Load the Excel file
#         wb = openpyxl.load_workbook(path)
#         # Get the first sheet of the workbook
#         sheet = wb.active
#         # Convert the sheet list
#         data = []
#         for row in sheet.iter_rows(values_only=True):
#             data.append(row)
#         title_row = data[0]
#         employee_data = []
#         for n in range(1, len(data)):
#             employee_detials = list(data[n])
#             employee_data.append(employee_detials)
#         all_employee_data = []
#         for num in range(0, len(employee_data)):
#             perticular_employee_data = {}
#             for x in range(0, len(title_row)):
#                 key = title_row[x]
#                 value = employee_data[num][x]
#                 perticular_employee_data.update({key: value})
#             all_employee_data.append(perticular_employee_data)
#         # print(all_employee_data)
#         # Store Data into Database
#         for details in all_employee_data:
#             id = str(details['Employee ID'])
#             if id == 'None':
#                 pass
#             else:
#                 month = datetime.datetime.now().month
#                 year = datetime.datetime.now().year
#                 doj = details['Date of Joining'].date()
#                 dob = details['Date of Birth'].date()
#                 print(dob)
#                 print(doj)
#                 personal_data = {
#                     'photo': 'photo',
#                     'employeeName': details['Employee Full Name'], 'userID': details['Employee ID'],
#                 }
#                 self.db.collection(companyname).document(u'employee').collection('employee').document(id).set(personal_data)
#
#                 total_leaves = {'CL': details['CL'], 'PL': details['PL'], 'SL': details['SL'], 'LWP': details['LWP']}
#
#                 self.db.collection(companyname).document(u'employee').collection('employee').document(id).collection(
#                     "leaveMST").document("total_leaves").set(total_leaves)
#                 salary_slip_data = {
#                     'employeeName': details['Employee Full Name'], 'userID': details['Employee ID'],
#                 }
#                 # self.db.collection(companyname).document('employee').collection('employee').document(id).collection(
#                 #     'salaryslips').document("sal00" + str({month})).set(salary_slip_data)
#             tds_detail = {
#                 'hlapplicationno': details['Home Loan Application No'],
#                 'hlamount': details['Home Loan Amount'],
#                 'hlperiod': details['Period of Home Loan'],
#             }
#
#             self.db.collection(companyname).document(u'employee').collection('employee').document(id).collection(
#                 "tdsmst").document("tds").set(tds_detail)
#
#
#
#
#
#
#
#
#
#
#
#
# import openpyxl
# import datetime
# import re
# from concurrent.futures import ThreadPoolExecutor
#
# class ExcelData():
#     def __init__(self, db):
#         self.db = db
#
#     def process_employee_data(self, companyname, details):
#         id = str(details['Employee ID'])
#         if id == 'None':
#             return
#         else:
#             month = datetime.datetime.now().month
#             year = datetime.datetime.now().year
#             doj = details['Date of Joining'].date()
#             dob = details['Date of Birth'].date()
#             print(dob)
#             print(doj)
#             personal_data = {
#                 'photo': 'photo',
#                 'employeeName': details['Employee Full Name'], 'userID': details['Employee ID'],
#                 'password': details['Password'], 'department': details['Department'],
#                 'email': details['Email'], 'salary': details['Salary'], 'jobPosition': details['Job Position'],
#                 'manager': details['Manager'], 'doj': f'{doj}',
#                 'currentExperience': details['Current Experience'], 'dob': f'{dob}',
#                 'gender': details['Gender'], 'phoneNo': details['Phone No'],
#                 'bankName': details['Bank Name'], 'accountHolderName': details['Account Holder Name'],
#                 'accountNumber': details['Account Number'], 'ifscCode': details['IFSC Code'],
#                 'aadharCardNo': details['Aadhar Card Number'], 'panCardNo': details['PAN Card No'],
#                 'passportNo': details['Passport No'],
#                 'pfAccountNo': details['PF Account No'], 'uanNo': details['UAN No'], 'esicNo': details['ESIC No']
#             }
#             self.db.collection(companyname).document(u'employee').collection('employee').document(id).set(personal_data)
#
#             total_leaves = {'CL': details['CL'], 'PL': details['PL'], 'SL': details['SL'], 'LWP': details['LWP']}
#
#             self.db.collection(companyname).document(u'employee').collection('employee').document(id).collection(
#                 "leaveMST").document("total_leaves").set(total_leaves)
#             salary_slip_data = {
#                 'employeeName': details['Employee Full Name'], 'userID': details['Employee ID'],
#                 'slip_id': f'sal00{month}', 'lwp': details['LWP'], 'basic': details['Basic'], 'da': details['DA'],
#                 'hra': details['HRA'], 'otherAllowance': details['Other Allowance'],
#                 'incentive': details['Incentive'],
#                 'grsOutstandingAdjustment': details['Grs Outstanding Adjustment'],
#                 'arrears': details['Arrears'], 'statutoryBonus': details['Statutory Bonus'],
#                 'grossSalary': details['Gross Salary'], 'epfo': details['EPFO'],
#                 'dedOutstandingAdjustment': details['Ded Outstanding Adjustment'], 'pt': details['PT'],
#                 'tds': details['TDS'], 'otherDeduction': details['Other Deduction'],
#                 'leaveDeduction': details['Leave Deduction'], 'netSalary': details['Net Salary'], 'month': month,
#                 'year': year,
#             }
#             # self.db.collection(companyname).document('employee').collection('employee').document(id).collection(
#             #     'salaryslips').document("sal00" + str({month})).set(salary_slip_data)
#             tds_detail = {
#                 'hlapplicationno': details['Home Loan Application No'],
#                 'hlamount': details['Home Loan Amount'],
#                 'hlperiod': details['Period of Home Loan'],
#                 'hlname': details['Home Loan Person Name'],
#                 'hlannual': details['Home Loan Interest'],
#                 'pino': details['Premium Insurance Number'],
#                 'piname': details['Premium Person Name'],
#                 'piannual': details['Premium Annual Amount'],
#                 'hipno': details['Health Insurance (Self) No'],
#                 'hipname': details['Health Insurance (Self) Person Name'],
#                 'hipannual': details['Health Insurance (Self) Annual Amount'],
#                 'hipperiod': details['Health Insurance (Self) Period'],
#                 'hisno': details['Health Insurance (Spouse) No'],
#                 'hisname': details['Health Insurance (Spouse) Person Name'],
#                 'hisannual': details['Health Insurance (Spouse) Annual Amount'],
#                 'hisperiod': details['Health Insurance (Spouse) Period'],
#                 'hifno': details['Health Insurance (Father) No'],
#                 'hifname': details['Health Insurance (Father) person Name'],
#                 'hifannual': details['Health Insurance (Father) Annual Amount'],
#                 'hifperiod': details['Health Insurance (Father) Period'],
#                 'ihlannual': details['Interest on Home Loan Payable'],
#                 'ihlpanlender': details['interest of Home Loan PAN of Lender'],
#                 'ihlname': details['Interest of Home loan Person Name'],
#                 'ahrmonth': details['Annual House Rent of Current Month'],
#                 'ahrlandpann': details['Rent House Landloard PAN'],
#                 'ahrperiod': details['Rent House Period'],
#                 'ahrlandname': details['Rent House Landloard Name'],
#                 'ahrlandaddress': details['Rent House Landloard Address'],
#                 'elssannual': details['ELSS Annual Amount'],
#                 'elssperiod': details['ELSS Period'],
#                 'tfannual': details['Tution Fees Annual Amount'],
#                 'tfperiod': details['Tution Fees Period']
#             }
#
#             self.db.collection(companyname).document(u'employee').collection('employee').document(id).collection(
#                 "tdsmst").document("tds").set(tds_detail)
#
#     def store_excel_data(self, companyname, path):
#         # Load the Excel file
#         wb = openpyxl.load_workbook(path)
#         # Get the first sheet of the workbook
#         sheet = wb.active
#         # Convert the sheet list
#         data = []
#         for row in sheet.iter_rows(values_only=True):
#             data.append(row)
#         title_row = data[0]
#         employee_data = []
#         for n in range(1, len(data)):
#             employee_details = list(data[n])
#             employee_data.append(employee_details)
#         all_employee_data = []
#         for num in range(0, len(employee_data)):
#             perticular_employee_data = {}
#             for x in range(0, len(title_row)):
#                 key = title_row[x]
#                 value = employee_data[num][x]
#                 perticular_employee_data.update({key: value})
#             all_employee_data.append(perticular_employee_data)
#
#         # Process employee data using a thread pool
#         with ThreadPoolExecutor() as executor:
#             for details in all_employee_data:
#                 executor.submit(self.process_employee_data, companyname, details)
#
#
#
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from details import Profile
# from salary_manage import Salarymanage
# import os
# import calendar
# from concurrent.futures import ThreadPoolExecutor
#
#
# def draw_my_rular(pdf):
#     ''' FOR GRID LAYOUT '''
#     pdf.drawString(100, 810, "x100")
#     pdf.drawString(200, 810, "x200")
#     pdf.drawString(300, 810, "x300")
#     pdf.drawString(400, 810, "x400")
#     pdf.drawString(500, 810, "x500")
#
#     pdf.drawString(10, 100, "y100")
#     pdf.drawString(10, 200, "y200")
#     pdf.drawString(10, 300, "y300")
#     pdf.drawString(10, 400, "y400")
#     pdf.drawString(10, 500, "y500")
#     pdf.drawString(10, 600, "y600")
#     pdf.drawString(10, 700, "y700")
#     pdf.drawString(10, 800, "y800")
#
#
# # draw_my_rular(pdf)
#
# class SalarySlip():
#
#     def __init__(self, db):
#         self.db = db
#
#     def salary_slip_personal(self, companyname,id, salid, path):
#         ''' CREATE SALARYSLIP PDF '''
#
#         empid = id
#
#         personal_data = Profile(self.db, empid,companyname).personal_data()
#
#         salary_data = Profile(self.db, empid,companyname).salary_data()[salid]
#
#         leave_data = Profile(self.db, empid,companyname).leave_data()[0]
#
#         mont_in_num = int(salid[5:])
#         month = calendar.month_name[mont_in_num]
#
#         pdf_location = f"{path}/Salaryslips_{empid}/{month}/"
#         if not os.path.exists(pdf_location):
#             os.makedirs(pdf_location)
#         filename = f'{empid}_{salid}.pdf'
#         pdf_file = pdf_location + filename
#         documentTitle = "SalarySlip!"
#         title = "ALIAN SOFTWARE"
#
#         textLines = {"Employee Name": personal_data["employeeName"],
#                      "Employee ID": personal_data["userID"],
#
#                      }
#
#         textLines_two = {"PAN No.": personal_data["panCardNo"],
#                          "UAN No.": personal_data["uanNo"],
#
#                          }
#
#
#         textLines_three = {"Basic Salary": salary_data["basic"],
#
#                            }
#
#         textLines_four = {"EPFO": salary_data["epfo"],
#
#                           }
#
#         pdf = canvas.Canvas(pdf_file)
#
#         pdf.setTitle(documentTitle)
#
#         # # # # # Company Name and Address # # # # #
#
#         pdf.setFont("Times-Bold", 22)
#         pdf.drawString(50, 790, title)
#
#         pdf.setFont("Times-Roman", 10)
#
#
#         pdf.setFont("Times-Roman", 10)
#
#
#         pdf.line(30, 740, 550, 740)
#
#         # # # # # Employee Pay Summary # # # # #
#
#         pdf.setFont("Times-Roman", 12)
#
#
#         pdf.setFont("Times-Bold", 16)
#
#
#         text = pdf.beginText(50, 650)
#         pdf.setFont("Times-Bold", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines.items():
#             text.textLines(key)
#         pdf.drawText(text)
#
#         text = pdf.beginText(200, 650)
#         pdf.setFont("Times-Roman", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines.items():
#             text.textLines(str(value))
#         pdf.drawText(text)
#
#         text = pdf.beginText(320, 650)
#         pdf.setFont("Times-Bold", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_two.items():
#             text.textLines(key)
#         pdf.drawText(text)
#
#         text = pdf.beginText(410, 650)
#         pdf.setFont("Times-Roman", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_two.items():
#             text.textLines(str(value))
#         pdf.drawText(text)
#
#         # Table Horizontal lines
#
#         pdf.setFont("Times-Roman", 10)
#         pdf.drawCentredString(425, 545, "Leave Balance")
#         pdf.drawCentredString(355, 525, "CL")
#         pdf.drawCentredString(425, 525, "SL")
#         pdf.drawCentredString(495, 525, "PL")
#         pdf.drawCentredString(355, 505, str(leave_data["CL"]))
#         pdf.drawCentredString(425, 505, str(leave_data["SL"]))
#         pdf.drawCentredString(495, 505, str(leave_data["PL"]))
#
#         pdf.line(30, 470, 550, 470)
#
#         # # # # # Amounts # # # # #
#
#         pdf.setFont("Times-Bold", 18)
#
#         pdf.drawString(50, 445, "Earning")
#
#         pdf.drawString(200, 445, "Amount")
#
#         pdf.drawString(320, 445, "Deduction")
#
#         pdf.drawString(470, 445, "Amount")
#
#         pdf.line(30, 430, 550, 430)
#
#         text = pdf.beginText(50, 400)
#         pdf.setFont("Times-Bold", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_three.items():
#             text.textLines(key)
#         pdf.drawText(text)
#
#         text = pdf.beginText(200, 400)
#         pdf.setFont("Times-Roman", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_three.items():
#             text.textLines(str(value))
#         pdf.drawText(text)
#
#         pdf.line(290, 470, 290, 220)
#
#         text = pdf.beginText(320, 400)
#         pdf.setFont("Times-Bold", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_four.items():
#             text.textLines(key)
#         pdf.drawText(text)
#
#         text = pdf.beginText(470, 400)
#         pdf.setFont("Times-Roman", 12)
#         text.setFillColor(colors.black)
#         for key, value in textLines_four.items():
#             text.textLines(str(value))
#         pdf.drawText(text)
#
#         pdf.line(30, 220, 550, 220)
#
#         pdf.setFont("Times-Bold", 15)
#         pdf.drawString(50, 195, "Gross Salary(A)")
#         pdf.setFont("Helvetica", 12)
#         pdf.drawString(200, 195, str(salary_data["grossSalary"]))
#
#         pdf.setFont("Times-Bold", 15)
#         pdf.drawString(320, 195, "Total Deductions(B)")
#         pdf.setFont("Times-Roman", 12)
#         pdf.drawString(470, 195, str(salary_data["totalDeduction"]))
#
#         pdf.line(30, 180, 550, 180)
#
#         # # # # # Footer # # # # #
#
#         pdf.setFont("Times-Bold", 18)
#         pdf.drawCentredString(290, 120, f"Total Net Payable = {salary_data['netSalary']} RS")
#
#         pdf.setFont("Times-Roman", 10)
#         pdf.drawCentredString(290, 30, "Note : This is electronically generated document")
#
#         pdf.showPage()
#         pdf.save()
#
#     def salary_slip(self, companyname, salid, path):
#         ''' CREATE SALARYSLIP PDF '''
#
#         salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid=salid, )
#         for i in salary_list:
#
#             empid = salary_list[i]["userID"]
#
#             personal_data = Profile(self.db, empid,companyname).personal_data()
#
#             salary_data = Profile(self.db, empid,companyname).salary_data()[salid]
#
#             leave_data = Profile(self.db, empid,companyname).leave_data()[0]
#
#             mont_in_num = int(salid[5:])
#             month = calendar.month_name[mont_in_num]
#
#             pdf_location = f"{path}/Salaryslips/{month}/"
#             if not os.path.exists(pdf_location):
#                 os.makedirs(pdf_location)
#             filename = f'{empid}_{salid}.pdf'
#             pdf_file = pdf_location + filename
#             documentTitle = "SalarySlip!"
#             title = "ALIAN SOFTWARE"
#             address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
#             address_line2 = "Indira Circle, Anand, Gujarat 388001"
#             subtitle = f"Pay Slip for the Month of {month}"
#             subtitle_one = "Employee Pay Summary"
#
#             textLines = {"Employee Name": personal_data["employeeName"],
#                          "Employee ID": personal_data["userID"],
#                          "Date of Joining": personal_data["doj"],
#                          "Branch": "Anand",
#                          "Designation": personal_data["jobPosition"],
#                          "Department": personal_data["department"],
#                          "Date of effectiveness": personal_data["doj"],
#                          "Week Offs": "",
#                          "Working Days": "",
#                          "LWP": salary_data['lwp']
#                          }
#
#             textLines_two = {"PAN No.": personal_data["panCardNo"],
#                              "UAN No.": personal_data["uanNo"],
#                              "PF No.": personal_data["pfAccountNo"],
#                              "ESIC No.": personal_data["esicNo"],
#                              "Bank Name": personal_data["bankName"],
#                              "Bank A/c No.": personal_data["accountNumber"],
#                              }
#
#             textLines_three = {"Basic Salary": salary_data["basic"],
#                                "HRA": salary_data["hra"],
#                                "DA": salary_data["da"],
#                                "Other Allowance": salary_data["otherAllowance"],
#                                "Incentive": salary_data["incentive"],
#                                "Arrears": salary_data["arrears"],
#                                "Outstanding Adjustment": salary_data["grsOutstandingAdjustment"],
#                                "Statutory Bonus": salary_data["statutoryBonus"],
#                                "Working Days": "",
#                                "LWP": salary_data["lwp"]
#                                }
#
#             textLines_four = {"EPFO": salary_data["epfo"],
#                               "TDS": salary_data["tds"],
#                               "PT": salary_data["pt"],
#                               "Leave Deduction": salary_data["leaveDeduction"],
#                               "Other Deduction": salary_data["otherDeduction"],
#                               "Outstanding Adjustment": salary_data["dedOutstandingAdjustment"],
#                               }
#
#             pdf = canvas.Canvas(pdf_file)
#
#             pdf.setTitle(documentTitle)
#
#             # # # # # Company Name and Address # # # # #
#
#             pdf.setFont("Times-Bold", 22)
#             pdf.drawString(50, 790, title)
#
#             pdf.setFont("Times-Roman", 10)
#             pdf.drawString(50, 770, address_line1)
#
#             pdf.setFont("Times-Roman", 10)
#             pdf.drawString(50, 755, address_line2)
#
#             pdf.line(30, 740, 550, 740)
#
#             # # # # # Employee Pay Summary # # # # #
#
#             pdf.setFont("Times-Roman", 12)
#             pdf.drawCentredString(290, 710, subtitle)
#
#             pdf.setFont("Times-Bold", 16)
#             pdf.drawCentredString(290, 680, subtitle_one)
#
#             text = pdf.beginText(50, 650)
#             pdf.setFont("Times-Bold", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines.items():
#                 text.textLines(key)
#             pdf.drawText(text)
#
#             text = pdf.beginText(200, 650)
#             pdf.setFont("Times-Roman", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines.items():
#                 text.textLines(str(value))
#             pdf.drawText(text)
#
#             text = pdf.beginText(320, 650)
#             pdf.setFont("Times-Bold", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_two.items():
#                 text.textLines(key)
#             pdf.drawText(text)
#
#             text = pdf.beginText(410, 650)
#             pdf.setFont("Times-Roman", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_two.items():
#                 text.textLines(str(value))
#             pdf.drawText(text)
#
#             # Table Horizontal lines
#             pdf.line(320, 560, 530, 560)
#             pdf.line(320, 540, 530, 540)
#             pdf.line(320, 520, 530, 520)
#             pdf.line(320, 500, 530, 500)
#
#             # Table Vertical lines
#             pdf.line(320, 560, 320, 500)
#             pdf.line(390, 540, 390, 500)
#             pdf.line(460, 540, 460, 500)
#             pdf.line(530, 560, 530, 500)
#
#             pdf.setFont("Times-Roman", 10)
#             pdf.drawCentredString(425, 545, "Leave Balance")
#             pdf.drawCentredString(355, 525, "CL")
#             pdf.drawCentredString(425, 525, "SL")
#             pdf.drawCentredString(495, 525, "PL")
#             pdf.drawCentredString(355, 505, str(leave_data["CL"]))
#             pdf.drawCentredString(425, 505, str(leave_data["SL"]))
#             pdf.drawCentredString(495, 505, str(leave_data["PL"]))
#
#             pdf.line(30, 470, 550, 470)
#
#             # # # # # Amounts # # # # #
#
#             pdf.setFont("Times-Bold", 18)
#
#             pdf.drawString(50, 445, "Earning")
#
#             pdf.drawString(200, 445, "Amount")
#
#             pdf.drawString(320, 445, "Deduction")
#
#             pdf.drawString(470, 445, "Amount")
#
#             pdf.line(30, 430, 550, 430)
#
#             text = pdf.beginText(50, 400)
#             pdf.setFont("Times-Bold", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_three.items():
#                 text.textLines(key)
#             pdf.drawText(text)
#
#             text = pdf.beginText(200, 400)
#             pdf.setFont("Times-Roman", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_three.items():
#                 text.textLines(str(value))
#             pdf.drawText(text)
#
#             pdf.line(290, 470, 290, 220)
#
#             text = pdf.beginText(320, 400)
#             pdf.setFont("Times-Bold", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_four.items():
#                 text.textLines(key)
#             pdf.drawText(text)
#
#             text = pdf.beginText(470, 400)
#             pdf.setFont("Times-Roman", 12)
#             text.setFillColor(colors.black)
#             for key, value in textLines_four.items():
#                 text.textLines(str(value))
#             pdf.drawText(text)
#
#             pdf.line(30, 220, 550, 220)
#
#             pdf.setFont("Times-Bold", 15)
#             pdf.drawString(50, 195, "Gross Salary(A)")
#             pdf.setFont("Helvetica", 12)
#             pdf.drawString(200, 195, str(salary_data["grossSalary"]))
#
#             pdf.setFont("Times-Bold", 15)
#             pdf.drawString(320, 195, "Total Deductions(B)")
#             pdf.setFont("Times-Roman", 12)
#             pdf.drawString(470, 195, str(salary_data["totalDeduction"]))
#
#             pdf.line(30, 180, 550, 180)
#
#             # # # # # Footer # # # # #
#
#             pdf.setFont("Times-Bold", 18)
#             pdf.drawCentredString(290, 120, f"Total Net Payable = {salary_data['netSalary']} RS")
#
#             pdf.setFont("Times-Roman", 10)
#             pdf.drawCentredString(290, 30, "Note : This is electronically generated document")
#
#             pdf.showPage()
#             pdf.save()
#
#
#
#
#
#
#
#
# def generate_salary_slip(salary_data, path):
#     empid = salary_data["userID"]
#     companyname = salary_data["companyname"]
#     personal_data = Profile(self.db, empid, companyname).personal_data()
#     salary_data = Profile(self.db, empid, companyname).salary_data()[salid]
#     leave_data = Profile(self.db, empid, companyname).leave_data()[0]
#     month_num = int(salid[5:])
#     month = calendar.month_name[month_num]
#     pdf_location = f"{path}/Salaryslips/{month}/"
#     if not os.path.exists(pdf_location):
#         os.makedirs(pdf_location)
#     filename = f'{empid}_{salid}.pdf'
#     pdf_file = pdf_location + filename
#     documentTitle = "SalarySlip!"
#     title = "ALIAN SOFTWARE"
#     address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
#     address_line2 = "Indira Circle, Anand, Gujarat 388001"
#     subtitle = f"Pay Slip for the Month of {month}"
#     subtitle_one = "Employee Pay Summary"
#
#     textLines = {"Employee Name": personal_data["employeeName"],
#                  "Employee ID": personal_data["userID"],
#                  "Date of Joining": personal_data["doj"],
#                  "Branch": "Anand",
#                  "Designation": personal_data["jobPosition"],
#                  "Department": personal_data["department"],
#                  "Date of effectiveness": personal_data["doj"],
#                  "Week Offs": "",
#                  "Working Days": "",
#                  "LWP": salary_data['lwp']
#                  }
#
#     textLines_two = {"PAN No.": personal_data["panCardNo"],
#                      "UAN No.": personal_data["uanNo"],
#                      "PF No.": personal_data["pfAccountNo"],
#                      "ESIC No.": personal_data["esicNo"],
#                      "Bank Name": personal_data["bankName"],
#                      "Bank A/c No.": personal_data["accountNumber"],
#                      }
#
#     textLines_three = {"Basic Salary": salary_data["basic"],
#                        "HRA": salary_data["hra"],
#                        "DA": salary_data["da"],
#                        "Other Allowance": salary_data["otherAllowance"],
#                        "Incentive": salary_data["incentive"],
#                        "Arrears": salary_data["arrears"],
#                        "Outstanding Adjustment": salary_data["grsOutstandingAdjustment"],
#                        "Statutory Bonus": salary_data["statutoryBonus"],
#                        "Working Days": "",
#                        "LWP": salary_data["lwp"]
#                        }
#
#     textLines_four = {"EPFO": salary_data["epfo"],
#                       "TDS": salary_data["tds"],
#                       "PT": salary_data["pt"],
#                       "Leave Deduction": salary_data["leaveDeduction"],
#                       "Other Deduction": salary_data["otherDeduction"],
#                       "Outstanding Adjustment": salary_data["dedOutstandingAdjustment"],
#                       }
#
#     pdf = canvas.Canvas(pdf_file)
#
#     pdf.setTitle(documentTitle)
#
#     # # # # # Company Name and Address # # # # #
#
#     pdf.setFont("Times-Bold", 22)
#     pdf.drawString(50, 790, title)
#
#     pdf.setFont("Times-Roman", 10)
#     pdf.drawString(50, 770, address_line1)
#
#     pdf.setFont("Times-Roman", 10)
#     pdf.drawString(50, 755, address_line2)
#
#     pdf.line(30, 740, 550, 740)
#
#     # # # # # Employee Pay Summary # # # # #
#
#     pdf.setFont("Times-Roman", 12)
#     pdf.drawCentredString(290, 710, subtitle)
#
#     pdf.setFont("Times-Bold", 16)
#     pdf.drawCentredString(290, 680, subtitle_one)
#
#     text = pdf.beginText(50, 650)
#     pdf.setFont("Times-Bold", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines.items():
#         text.textLines(key)
#     pdf.drawText(text)
#
#     text = pdf.beginText(200, 650)
#     pdf.setFont("Times-Roman", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines.items():
#         text.textLines(str(value))
#     pdf.drawText(text)
#
#     text = pdf.beginText(320, 650)
#     pdf.setFont("Times-Bold", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_two.items():
#         text.textLines(key)
#     pdf.drawText(text)
#
#     text = pdf.beginText(410, 650)
#     pdf.setFont("Times-Roman", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_two.items():
#         text.textLines(str(value))
#     pdf.drawText(text)
#
#     # Table Horizontal lines
#     pdf.line(320, 560, 530, 560)
#     pdf.line(320, 540, 530, 540)
#     pdf.line(320, 520, 530, 520)
#     pdf.line(320, 500, 530, 500)
#
#     # Table Vertical lines
#     pdf.line(320, 560, 320, 500)
#     pdf.line(390, 540, 390, 500)
#     pdf.line(460, 540, 460, 500)
#     pdf.line(530, 560, 530, 500)
#
#     pdf.setFont("Times-Roman", 10)
#     pdf.drawCentredString(425, 545, "Leave Balance")
#     pdf.drawCentredString(355, 525, "CL")
#     pdf.drawCentredString(425, 525, "SL")
#     pdf.drawCentredString(495, 525, "PL")
#     pdf.drawCentredString(355, 505, str(leave_data["CL"]))
#     pdf.drawCentredString(425, 505, str(leave_data["SL"]))
#     pdf.drawCentredString(495, 505, str(leave_data["PL"]))
#
#     pdf.line(30, 470, 550, 470)
#
#     # # # # # Amounts # # # # #
#
#     pdf.setFont("Times-Bold", 18)
#
#     pdf.drawString(50, 445, "Earning")
#
#     pdf.drawString(200, 445, "Amount")
#
#     pdf.drawString(320, 445, "Deduction")
#
#     pdf.drawString(470, 445, "Amount")
#
#     pdf.line(30, 430, 550, 430)
#
#     text = pdf.beginText(50, 400)
#     pdf.setFont("Times-Bold", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_three.items():
#         text.textLines(key)
#     pdf.drawText(text)
#
#     text = pdf.beginText(200, 400)
#     pdf.setFont("Times-Roman", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_three.items():
#         text.textLines(str(value))
#     pdf.drawText(text)
#
#     pdf.line(290, 470, 290, 220)
#
#     text = pdf.beginText(320, 400)
#     pdf.setFont("Times-Bold", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_four.items():
#         text.textLines(key)
#     pdf.drawText(text)
#
#     text = pdf.beginText(470, 400)
#     pdf.setFont("Times-Roman", 12)
#     text.setFillColor(colors.black)
#     for key, value in textLines_four.items():
#         text.textLines(str(value))
#     pdf.drawText(text)
#
#     pdf.line(30, 220, 550, 220)
#
#     pdf.setFont("Times-Bold", 15)
#     pdf.drawString(50, 195, "Gross Salary(A)")
#     pdf.setFont("Helvetica", 12)
#     pdf.drawString(200, 195, str(salary_data["grossSalary"]))
#
#     pdf.setFont("Times-Bold", 15)
#     pdf.drawString(320, 195, "Total Deductions(B)")
#     pdf.setFont("Times-Roman", 12)
#     pdf.drawString(470, 195, str(salary_data["totalDeduction"]))
#
#     pdf.line(30, 180, 550, 180)
#
#     # # # # # Footer # # # # #
#
#     pdf.setFont("Times-Bold", 18)
#     pdf.drawCentredString(290, 120, f"Total Net Payable = {salary_data['netSalary']} RS")
#
#     pdf.setFont("Times-Roman", 10)
#     pdf.drawCentredString(290, 30, "Note : This is electronically generated document")
#
#     pdf.showPage()
#     pdf.save()
#
# def generate_salary_slips(salary_list, path):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#         futures = []
#         for salary_data in salary_list:
#             future = executor.submit(generate_salary_slip, salary_data, path)
#             futures.append(future)
#         for future in concurrent.futures.as_completed(futures):
#             try:
#                 result = future.result()
#             except Exception as exc:
#                 print(f"Exception generated: {exc}")
#
# if __name__ == "__main__":
#     salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid=salid, )
#     generate_salary_slips(salary_list, path)
#
#
#
# import concurrent.futures

































class SalarySlip():

    def __init__(self, db):
        self.db = db



    def salary_slip(self, companyname, salid, path):
        ''' CREATE SALARYSLIP PDF '''

        salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid=salid, )
        for i in salary_list:

            empid = salary_list[i]["userID"]

            personal_data = Profile(self.db, empid,companyname).personal_data()

            salary_data = Profile(self.db, empid,companyname).salary_data()[salid]

            leave_data = Profile(self.db, empid,companyname).leave_data()[0]

            mont_in_num = int(salid[5:])
            month = calendar.month_name[mont_in_num]

            pdf_location = f"{path}/Salaryslips/{month}/"
            if not os.path.exists(pdf_location):
                os.makedirs(pdf_location)
            filename = f'{empid}_{salid}.pdf'
            pdf_file = pdf_location + filename
            documentTitle = "SalarySlip!"
            title = "ALIAN SOFTWARE"
            address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
            address_line2 = "Indira Circle, Anand, Gujarat 388001"
            subtitle = f"Pay Slip for the Month of {month}"
            subtitle_one = "Employee Pay Summary"

            textLines = {"Employee Name": personal_data["employeeName"],}

            textLines_two = {"PAN No.": personal_data["panCardNo"],
                             "UAN No.": personal_data["uanNo"],
                             "PF No.": personal_data["pfAccountNo"],
                             "ESIC No.": personal_data["esicNo"],
                             "Bank Name": personal_data["bankName"],
                             "Bank A/c No.": personal_data["accountNumber"],
                             }

            textLines_three = {"Basic Salary": salary_data["basic"],
                               "HRA": salary_data["hra"],
                               }

            textLines_four = {"EPFO": salary_data["epfo"],
                              "TDS": salary_data["tds"],  }

            pdf = canvas.Canvas(pdf_file)

            pdf.setTitle(documentTitle)

            # # # # # Company Name and Address # # # # #

            pdf.setFont("Times-Bold", 22)
            pdf.drawString(50, 790, title)


            pdf.showPage()
            pdf.save()

# SalarySlip.salary_slip('EMP003')





















import threading

class SalarySlip():

    def __init__(self, db):
        self.db = db

    def generate_slip(self, empid, companyname, salid, path):
        personal_data = Profile(self.db, empid, companyname).personal_data()
        salary_data = Profile(self.db, empid, companyname).salary_data()[salid]
        leave_data = Profile(self.db, empid, companyname).leave_data()[0]
        mont_in_num = int(salid[5:])
        month = calendar.month_name[mont_in_num]
        pdf_location = f"{path}/Salaryslips/{month}/"
        if not os.path.exists(pdf_location):
            os.makedirs(pdf_location)
        filename = f'{empid}_{salid}.pdf'
        pdf_file = pdf_location + filename
        documentTitle = "SalarySlip!"
        title = "ALIAN SOFTWARE"
        address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
        address_line2 = "Indira Circle, Anand, Gujarat 388001"
        subtitle = f"Pay Slip for the Month of {month}"
        subtitle_one = "Employee Pay Summary"
        textLines = {"Employee Name": personal_data["employeeName"]}
        textLines_two = {"PAN No.": personal_data["panCardNo"],
                         "UAN No.": personal_data["uanNo"],
                         "PF No.": personal_data["pfAccountNo"],
                         "ESIC No.": personal_data["esicNo"],
                         "Bank Name": personal_data["bankName"],
                         "Bank A/c No.": personal_data["accountNumber"]}
        textLines_three = {"Basic Salary": salary_data["basic"],
                           "HRA": salary_data["hra"]}
        textLines_four = {"EPFO": salary_data["epfo"],
                          "TDS": salary_data["tds"]}
        pdf = canvas.Canvas(pdf_file)
        pdf.setTitle(documentTitle)
        pdf.setFont("Times-Bold", 22)
        pdf.drawString(50, 790, title)
        pdf.showPage()
        pdf.save()

    def salary_slip(self, companyname, salid, path):
        ''' CREATE SALARYSLIP PDF '''
        salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid=salid, )
        threads = []
        for i in salary_list:
            empid = salary_list[i]["userID"]
            thread = threading.Thread(target=self.generate_slip, args=(empid, companyname, salid, path))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()












from concurrent.futures import ThreadPoolExecutor

class SalarySlip():

    def __init__(self, db):
        self.db = db

    def create_salary_slip(self, empid, companyname, salid, path):
        ''' CREATE SALARYSLIP PDF '''

        personal_data = Profile(self.db, empid,companyname).personal_data()
        salary_data = Profile(self.db, empid,companyname).salary_data()[salid]
        mont_in_num = int(salid[5:])
        month = calendar.month_name[mont_in_num]

        pdf_location = f"{path}/Salaryslips/{month}/"
        if not os.path.exists(pdf_location):
            os.makedirs(pdf_location)
        filename = f'{empid}_{salid}.pdf'
        pdf_file = pdf_location + filename
        documentTitle = "SalarySlip!"
        title = "ALIAN SOFTWARE"
        address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
        address_line2 = "Indira Circle, Anand, Gujarat 388001"
        subtitle = f"Pay Slip for the Month of {month}"
        subtitle_one = "Employee Pay Summary"

        textLines = {"Employee Name": personal_data["employeeName"], }

        textLines_two = {"PAN No.": personal_data["panCardNo"],
                         "UAN No.": personal_data["uanNo"],
                         "PF No.": personal_data["pfAccountNo"],
                         "ESIC No.": personal_data["esicNo"],
                         "Bank Name": personal_data["bankName"],
                         "Bank A/c No.": personal_data["accountNumber"],
                         }

        textLines_three = {"Basic Salary": salary_data["basic"],
                           "HRA": salary_data["hra"],
                           }

        textLines_four = {"EPFO": salary_data["epfo"],
                          "TDS": salary_data["tds"], }

        pdf = canvas.Canvas(pdf_file)

        pdf.setTitle(documentTitle)

        # # # # # Company Name and Address # # # # #

        pdf.setFont("Times-Bold", 22)
        pdf.drawString(50, 790, title)

        pdf.showPage()
        pdf.save()

    def salary_slip(self, companyname, salid, path):
        ''' CREATE SALARYSLIP PDF '''

        salary_list = Salarymanage(self.db).get_all_emp_salary_data(salid=salid, )

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for i in salary_list:
                empid = salary_list[i]["userID"]
                futures.append(executor.submit(self.create_salary_slip, empid, companyname, salid, path))

            for future in futures:
                future.result()
