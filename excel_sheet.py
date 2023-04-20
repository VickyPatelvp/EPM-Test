import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Select the active worksheet
worksheet = workbook.active

A1 = worksheet.merge_cells('A1:Z1')

# Write some data to the worksheet

worksheet.title = "Company Name"

worksheet['A1'] = 'Bank Name Associated With Company'


title_row = ["Sr. No" , "Employee Name", "Bank Name", "Account No", "Total Salary"]
worksheet.append(title_row)


# Save the workbook
workbook.save('example.xlsx')
