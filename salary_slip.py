from reportlab.pdfgen import canvas
from reportlab.lib import colors
from details import Profile

profile = Profile('1')
personal_data = profile.personal_data()

salary_data = profile.salary_data()

# FOR LAYOUT


def draw_my_rular(pdf):
    pdf.drawString(100, 810, "x100")
    pdf.drawString(200, 810, "x200")
    pdf.drawString(300, 810, "x300")
    pdf.drawString(400, 810, "x400")
    pdf.drawString(500, 810, "x500")

    pdf.drawString(10, 100, "y100")
    pdf.drawString(10, 200, "y200")
    pdf.drawString(10, 300, "y300")
    pdf.drawString(10, 400, "y400")
    pdf.drawString(10, 500, "y500")
    pdf.drawString(10, 600, "y600")
    pdf.drawString(10, 700, "y700")
    pdf.drawString(10, 800, "y800")


# draw_my_rular(pdf)


def salary_slip(id):

    profile = Profile(id)

    personal_data = profile.personal_data()

    salary_data = profile.salary_data()

    leave_data = profile.leave_data()

    filename = 'SalarySlip.pdf'
    documentTitle = "SalarySlip!"
    title = "ALIAN SOFTWARE"
    address_line1 = "Shreeji Arcade, 2nd Floor, Opp Shasvat Hospital,"
    address_line2 = "Indira Circle, Anand, Gujarat 388001"
    subtitle = "Pay Slip for the Month of 1"
    subtitle_one = "Employee Pay Summary"

    textLines = {"Employee Name": personal_data["employeeName"],
                 "Employee ID": personal_data["userID"],
                 "Date of Joining": personal_data["doj"],
                 "Branch": "Anand",
                 "Designation": personal_data["jobPosition"],
                 "Department": personal_data["department"],
                 "Date of effectiveness": personal_data["doj"],
                 "Week Offs": "",
                 "Working Days": "",
                 "LWP": salary_data["lwp"]
                 }

    textLines_two = {"PAN No.": personal_data["panCardNo"],
                     "UAN No.": personal_data["uanNo"],
                     "PF No.": personal_data["pfAccountNo"],
                     "ESIC No.": personal_data["esicNo"],
                     "Bank Name": personal_data["bankName"],
                     "Bank A/c No.": personal_data["accountNumber"],
                     }

    textLines_three = {"Basic Salary": salary_data["basic"],
                       "HRA": salary_data["hra"],
                       "DA": salary_data["da"],
                       "Other Allowance": salary_data["otherAllowance"],
                       "Incentive": salary_data["incentive"],
                       "Arrears": salary_data["arrears"],
                       "Outstanding Adjustments": salary_data["outstandingAdjustment"],
                       "Statutory Bonus": salary_data["statutoryBonus"],
                       "Working Days": "",
                       "LWP": salary_data["lwp"]
                       }

    textLines_four = {"EPFO": salary_data["epfo"],
                      "TDS": salary_data["tds"],
                      "PT": salary_data["pt"],
                      "Leave Deduction": salary_data["leaveDeduction"],
                      "Other Deduction": salary_data["otherDeduction"],
                      "Outstanding Adjustments": salary_data["outstandingAdjustments"],
                      }

    pdf = canvas.Canvas(filename=filename)

    pdf.setTitle(documentTitle)

    # # # # # Company Name and Address # # # # #

    pdf.setFont("Times-Bold", 22)
    pdf.drawString(50, 790, title)

    pdf.setFont("Times-Roman", 10)
    pdf.drawString(50, 770, address_line1)

    pdf.setFont("Times-Roman", 10)
    pdf.drawString(50, 755, address_line2)

    pdf.line(30, 740, 550, 740)

    # # # # # Employee Pay Summary # # # # #

    pdf.setFont("Times-Roman", 12)
    pdf.drawCentredString(290, 710, subtitle)

    pdf.setFont("Times-Bold", 16)
    pdf.drawCentredString(290, 680, subtitle_one)

    text = pdf.beginText(50, 650)
    pdf.setFont("Times-Bold", 12)
    text.setFillColor(colors.black)
    for key, value in textLines.items():
        text.textLines(key)
    pdf.drawText(text)

    text = pdf.beginText(200, 650)
    pdf.setFont("Times-Roman", 12)
    text.setFillColor(colors.black)
    for key, value in textLines.items():
        text.textLines(value)
    pdf.drawText(text)

    text = pdf.beginText(320, 650)
    pdf.setFont("Times-Bold", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_two.items():
        text.textLines(key)
    pdf.drawText(text)

    text = pdf.beginText(410, 650)
    pdf.setFont("Times-Roman", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_two.items():
        text.textLines(value)
    pdf.drawText(text)

    # Table Horizontal lines
    pdf.line(320, 560, 530, 560)
    pdf.line(320, 540, 530, 540)
    pdf.line(320, 520, 530, 520)
    pdf.line(320, 500, 530, 500)

    # Table Vertical lines
    pdf.line(320, 560, 320, 500)
    pdf.line(390, 540, 390, 500)
    pdf.line(460, 540, 460, 500)
    pdf.line(530, 560, 530, 500)

    pdf.setFont("Times-Roman", 10)
    pdf.drawCentredString(425, 545, "Leave Balance")
    pdf.drawCentredString(355, 525, "CL")
    pdf.drawCentredString(425, 525, "SL")
    pdf.drawCentredString(495, 525, "PL")
    pdf.drawCentredString(355, 505, leave_data[1]["CL"])
    pdf.drawCentredString(425, 505, leave_data[1]["SL"])
    pdf.drawCentredString(495, 505, leave_data[1]["PL"])

    pdf.line(30, 470, 550, 470)

    # # # # # Amounts # # # # #

    pdf.setFont("Times-Bold", 18)

    pdf.drawString(50, 445, "Earning")

    pdf.drawString(200, 445, "Amount")

    pdf.drawString(320, 445, "Deduction")

    pdf.drawString(470, 445, "Amount")

    pdf.line(30, 430, 550, 430)

    text = pdf.beginText(50, 400)
    pdf.setFont("Times-Bold", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_three.items():
        text.textLines(key)
    pdf.drawText(text)

    text = pdf.beginText(200, 400)
    pdf.setFont("Times-Roman", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_three.items():
        text.textLines(value)
    pdf.drawText(text)

    pdf.line(290, 470, 290, 220)

    text = pdf.beginText(320, 400)
    pdf.setFont("Times-Bold", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_four.items():
        text.textLines(key)
    pdf.drawText(text)

    text = pdf.beginText(470, 400)
    pdf.setFont("Times-Roman", 12)
    text.setFillColor(colors.black)
    for key, value in textLines_four.items():
        text.textLines(value)
    pdf.drawText(text)

    pdf.line(30, 220, 550, 220)

    pdf.setFont("Times-Bold", 15)
    pdf.drawString(50, 195, "Gross Salary(A)")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(200, 195, salary_data["grossSalary"])

    pdf.setFont("Times-Bold", 15)
    pdf.drawString(320, 195, "Total Deductions(B)")
    pdf.setFont("Times-Roman", 12)
    pdf.drawString(470, 195, salary_data["totalDeduction"])

    pdf.line(30, 180, 550, 180)

    # # # # # Footer # # # # #

    pdf.setFont("Times-Bold", 18)
    pdf.drawCentredString(290, 120, f"Total Net Payable = {salary_data['netSalary']} RS")

    pdf.setFont("Times-Roman", 10)
    pdf.drawCentredString(290, 30, "Note : This is electronically generated document")

    pdf.showPage()
    pdf.save()


salary_slip('1')
