import datetime
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
# import localStorage as localStorage
from flask import Flask, render_template, request, redirect, url_for, session, send_file, Response
import io
from leave_manage import Leavemanage
from firebase_admin import credentials
from firebase_admin import firestore
from details import Profile
from create_new_employee import Create
from salary_manage import Salarymanage
from department import Department
from tds_data import TDSData
from update_employee import Update_information
from dashboard import Dashboard
import re
from excel_sheet import SalaryData
import concurrent.futures
from salary_slip import SalarySlip
from register import Register
from login import Login
from moth_days import Month_count
from mail import Mail

from salary_calculation import SalaryCalculation
from openpyxl import load_workbook

from generate_excel import create_excel_file
import pandas as pd
from read_data import ExcelData

# FLASK APP
app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
app.config['SESSION_TYPE'] = 'filesystem'

# USE A SERVICE ACCOUNT

cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-1602329ca8.json')
db = firestore.client()

leaveobj = Leavemanage(db)
dept = Department(db)
update_obj = Update_information(db)
dashboard_obj = Dashboard(db)
register_obj = Register(db)
login_obj = Login(db)
moth_count = Month_count()
mail_obj = Mail()


# Testing path
# C:/Users/alian/Desktop/Testing
        # C:/Users/alian/Downloads/my_file.xlsx


@app.route('/<companyname>/login/', methods=["POST", "GET"])
def login(companyname):
    responce = ''
    if request.method == 'POST':
        data = request.form
        responce = login_obj.login(data, companyname)

        if responce == 'Admin':
            # session['companyname']=companyname
            return redirect(url_for('dashboard', companyname=companyname, username=responce))
        elif responce != False:
            if responce['type'] == 'HR':
                return redirect(url_for('dashboard', companyname=companyname, username=responce['name']))
            else:
                return redirect(url_for('employee_profile', companyname=companyname, username=responce['name'],
                                        id=responce['empid']))
        else:
            responce = 'Inavalid Id and Password'
    ''' LOGIN PAGE '''
    url = f'/{companyname}/login'
    return render_template('login.html', responce=responce, url=url, companyname=companyname)


@app.route('/<companyname>/forgot_password', methods=["POST", "GET"])
def forgot_password(companyname):
    if request.method == 'POST':
        email = request.json["email"]
        print(email)
        if email != None:
            Admin = db.collection(companyname).document('admin').get().to_dict()
            if Admin != None:
                company_mail = Admin['AdminID']
                auth_password = Admin['auth_password']
                if company_mail == email:
                    email = email
                    password = Admin['password']
                    mail_obj.forgot_mail(email=email, companyname=companyname, password=password,
                                         company_mail=company_mail, auth_password=auth_password)
                else:
                    user = db.collection(companyname).document('employee').collection('employee').where(
                        'email', "==", email).get()
                    if user != None:
                        data = user[0].to_dict()
                        email = email
                        password = data['password']
                        mail_obj.forgot_mail(email=email, companyname=companyname, password=password,
                                             company_mail=company_mail, auth_password=auth_password)
    responce = 'invalid email'
    return redirect(url_for('login', companyname=companyname))


@app.route('/success', methods=["POST", "GET"])
def success():
    return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def register():
    responce = ''
    if request.method == 'POST':
        data = request.form
        responce = register_obj.register(data)
        if responce == True:
            return redirect(url_for('success'))

    ''' REGISTER PAGE '''
    return render_template('register.html', responce=responce)


@app.route('/<companyname>/<username>/dashboard', methods=['GET', 'POST'])
def dashboard(companyname, username):
    print('sfgasdfvhfvhvfhv')
    session.pop('excel_path', default=None)

    if request.method == 'POST':
        form = request.form.to_dict()
        # print(form)
        data = {str(form["date"]): form["description"]}
        db.collection(companyname).document('holidays').update(data)
        holidays = db.collection(companyname).document('holidays').get().to_dict()
        moath_data = moth_count.count(holidays)
        db.collection(companyname).document('month_data').set(moath_data)

    holidays = db.collection(companyname).document('holidays').get().to_dict()
    moath_data = moth_count.count(holidays)
    working_days = moath_data['workingDays']
    if datetime.datetime.now().day == 1:
        SalaryCalculation(db).generate_salary(companyname=companyname, workingday=working_days)
        leaveobj.leave_add(companyname)
    if datetime.datetime.today().day == 1 and datetime.datetime.today().month == 1:
        leaveobj.leave_reset(companyname)


    dashboard_data = dashboard_obj.all_data(companyname)

    ''' DISPLAY DASHBOARD '''

    holidays = moth_count.get_holidays(holidays)
    employee_on_leave, total_leaves, employee_birthday, employee_anniversary = dashboard_obj.Dashboard_data(companyname)
    return render_template('dashboard.html', employee_on_leave=employee_on_leave, total_leaves=total_leaves,
                           employee_birthday=employee_birthday, employee_anniversary=employee_anniversary,
                           moath_data=moath_data, companyname=companyname, holidays=holidays, username=username,
                           dashboard_data=dashboard_data)


@app.route('/<companyname>/<username>/employeelist', methods=['GET', 'POST'])
def employee_list(companyname, username):
    if request.method == 'POST':
        employee_mail = request.form.get('new_email')
        auth_data = db.collection(companyname).document('admin').get().to_dict()
        company_mail = auth_data['AdminID']
        auth_password = auth_data['auth_password']
        mail_obj.new_employee_mail(employee_mail, companyname, company_mail, auth_password)

    ''' DISPLAY LIST OF EMPLOYEES IN COMPANY '''

    def get_employee_data():

        docs = db.collection(companyname).document(u'employee').collection('employee').stream()
        employee_list = {}
        for doc in docs:
            employee_list.update({doc.id: doc.to_dict()})
        return employee_list

    def get_department_data():
        department = (db.collection(companyname).document(u'department').get()).to_dict()
        return department

    with concurrent.futures.ThreadPoolExecutor() as executor:
        employee_data = executor.submit(get_employee_data)
        department_data = executor.submit(get_department_data)

    employee_list = employee_data.result()
    department = department_data.result()
    return render_template('employees_list.html', data=employee_list, department=department, companyname=companyname,
                           username=username)


@app.route("/<companyname>/<username>/storage-path", methods=["POST"])
def excel_sheet_path(companyname, username):
    excel_path = request.json["excel_path"]
    excel = ExcelData(db)
    excel.store_excel_data(companyname, excel_path)
    return redirect(url_for('dashboard', companyname=companyname, username=username))


@app.route('/<companyname>/<username>/result', methods=['POST', 'GET'])
def add(companyname, username):
    ''' NEW EMPLOYEE DATA STORE IN DATABASE AND DISPLAY IN LIST '''
    create = Create(db, companyname)
    create.result()
    employee_mail = request.form.get('email')
    auth_data = db.collection(companyname).document('admin').get().to_dict()
    company_mail = auth_data['AdminID']
    auth_password = auth_data['auth_password']
    mail_obj.employee_registered_mail(employee_mail, companyname, company_mail, auth_password)
    return redirect(url_for('employee_list', companyname=companyname, username=username))


@app.route('/<companyname>/<username>/<id>/delete', methods=['POST', 'GET'])
def delete_employee(companyname, username, id):
    doc_ref = db.collection(companyname).document(u'employee').collection('employee').document(id)
    doc_ref.delete()
    return redirect(url_for('employee_list', companyname=companyname, username=username))


@app.route('/<companyname>/register_employee', methods=['POST', 'GET'])
def employee_register_by_mail(companyname):
    if request.method == 'POST':
        create = Create(db, companyname)
        create.result()
        email = request.form.get('email')
        auth_data = db.collection(companyname).document('admin').get().to_dict()
        company_mail = auth_data['AdminID']
        auth_password = auth_data['auth_password']
        mail_obj.employee_registered_mail(email, companyname, company_mail, auth_password)

        return redirect(url_for('success'))

    def get_department_data():
        department = (db.collection(companyname).document(u'department').get()).to_dict()
        return department

    with concurrent.futures.ThreadPoolExecutor() as executor:
        department_data = executor.submit(get_department_data)
    department = get_department_data()
    return render_template('add_employee.html', companyname=companyname, department=department,
                           department_data=department_data)


@app.route('/create_excel')
def create_excel():
    ''' EXCEL SHEET DATA FORMATE FOR NEW COMPANY '''
    # Create the Excel file
    wb = create_excel_file()

    # Save the file to a BytesIO object
    excel_file = io.BytesIO()
    wb.save(excel_file)
    excel_file.seek(0)

    # Return the file as a response with appropriate headers
    return Response(
        excel_file,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={
            "Content-Disposition": "attachment;filename=my_file.xlsx",
            "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        }
    )


@app.route('/<companyname>/upload_file', methods=['POST'])
def upload_file(companyname):
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            workbook = load_workbook(filename=file)
            worksheet = workbook.active
            data = []
            for row in worksheet.iter_rows(values_only=True):
                data.append(row)
            return redirect(url_for('employee_list', companyname=companyname))
    return redirect(url_for('employee_list', companyname=companyname))


@app.route('/<companyname>/<username>/employeeprofile/<id>', methods=['GET', 'POST'])
def employee_profile(companyname, username, id):
    ''' DISPLAY EMPLOYEE DETAILS '''
    users_ref = db.collection(str(companyname)).document('employee').collection('employee').document(id).collection(
        'leaveMST')
    if request.method == 'POST':
        ''' Store leave Data '''
        result = request.form

        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(leaveobj.take_leave, users_ref, data=result)

    ''' GET LEAVE DATA '''
    with ThreadPoolExecutor(max_workers=2) as executor:
        total_leave_future = executor.submit(leaveobj.get_total_leave, users_ref)
        leave_list_future = executor.submit(leaveobj.leave_list, users_ref)

    total_leave = total_leave_future.result()
    leave_list = leave_list_future.result()

    ''' GET EMPLOYEE DATA '''
    with ThreadPoolExecutor(max_workers=2) as executor:
        personal_data_future = executor.submit(Profile(db, id, companyname).personal_data)
        tds_data_future = executor.submit(Profile(db, id, companyname).tds_data)
        salary_data_future = executor.submit(Profile(db, id, companyname).salary_data)

    data = {'personal_data': personal_data_future.result(), 'tds_data': tds_data_future.result(),
            'salary_data': salary_data_future.result()}

    leave_status = False
    leave_status_date = ''
    for i in leave_list:
        if i != 'total_leaves':
            leave_date = (datetime.datetime.strptime(leave_list[i]['applydate'], '%Y-%m-%d').month)
            if leave_date == datetime.datetime.today().month:
                leave_status = True
                leave_status_date = (f'{leave_list[i]["fromdate"]} to {leave_list[i]["todate"]} ')

    return render_template('employee_profile.html', leave=leave_status, data=data, total_leave=total_leave,
                           leave_list=leave_list, companyname=companyname, leave_date=leave_status_date,
                           username=username)


@app.route('/<companyname>/<username>/pdf/<id>/<salid>')
def pdf_personal(companyname, username, id, salid):
    ''' SALARY SLIP PDF GENERATION '''
    if 'storage_path' in session:
        path = session["storage_path"]
        salary = SalarySlip(db)
        salary.salary_slip_personal(companyname, id, salid, path)
        return redirect(url_for('employee_profile', companyname=companyname, id=id, salid=salid, username=username))


@app.route('/<companyname>/<username>/personal_data_update/<id>', methods=['GET', 'POST'])
def personal_data_update(companyname, username, id):
    ''' UPDATE EMPLOYEE PERSONAL DETAILS '''
    if request.method == 'POST':
        form = request.get_json()
        update_obj.update_personal_info(companyname, form, id)
        return redirect(url_for('employee_profile', id=id, companyname=companyname, username=username))


@app.route('/<companyname>/<username>/tds_data_update/<id>', methods=['GET', 'POST'])
def tds_data_update(companyname, username, id):
    ''' UPDATE EMPLOYEE TDS DETAILS '''
    if request.method == 'POST':
        form = request.get_json()
        update_obj.update_tds_info(companyname, form, id)
    return redirect(url_for('employee_profile', id=id, companyname=companyname, username=username))


@app.route('/<companyname>/<username>/department', methods=['GET', 'POST'])
def department(companyname, username):
    ''' DISPLAY DEPARTMENT '''
    if request.method == 'POST':
        ''' Add New DEPARTMENT '''
        result = request.form
        dept.add_department(companyname, result)
    doc_ref = db.collection(str(companyname)).document(u'department')
    data = doc_ref.get().to_dict()
    return render_template('department.html', data=data, obj=dept, companyname=companyname, username=username)


@app.route('/<companyname>/<username>/delete_department/<dep> <pos>', methods=['GET', 'POST'])
def delete_department(companyname, username, dep, pos):
    ''' DELETE DEPARTMENT '''
    a = dep, pos
    pattern = r'[^a-zA-Z\d\s]'
    # Use the re.sub() function to replace all occurrences of the pattern with an empty string
    dep = re.sub(pattern, '', dep)
    pos = re.sub(pattern, '', pos)
    dept.delete_department(companyname, dep, pos)
    return redirect(url_for('department', companyname=companyname, username=username))


@app.route("/set-storage-path", methods=["POST"])
def set_storage_path():
    path = request.json["path"]
    salary = SalarySlip(db)
    salary.salary_slip(companyname, salid, path)
    return redirect(url_for('salary', companyname=companyname, username=username, salid=salid))


@app.route('/<companyname>/<username>/salary', methods=['GET', 'POST'])
def salary(companyname, username):
    ''' DISPLAY SALARY DETAILS OF ALL MONTH IN YEAR '''
    if request.method == 'POST':
        form = request.form
        data_dict = {}
        for key, value in form.items():
            if value != '':
                data_dict.update({key: value})
        # ADD Salary Criteria
        docs = db.collection(companyname).document('salary_calc')

        if len(docs.get().to_dict()) == 0:
            db.collection(companyname).document('salary_calc').set(data_dict)
        else:
            db.collection(companyname).document('salary_calc').update(data_dict)
    salary_criteria = db.collection(str(companyname)).document('salary_calc').get().to_dict()
    salary_list = Salarymanage(db).get_all_month_salary_data(companyname)
    salary_status = db.collection(companyname).document('salary_status').get().to_dict()
    return render_template('salary_sheet_month.html', data=salary_list, salary_criteria=salary_criteria,
                           companyname=companyname, username=username, salary_status=salary_status)


@app.route('/<companyname>/<username>/salarysheetview/<salid>', methods=['GET', 'POST'])
def salary_sheet_view(companyname, username, salid):
    # month = int(salid[5:])
    if request.method == 'POST':
        form = request.form
        fields = {}
        for key, value in form.items():
            fields.update({key: value})
        if 'storage_path' in session:
            path = session["storage_path"]

        salary_excel = SalaryData(db)
        salary_excel.add_data(companyname=companyname, salid=salid, fields=fields, path=path)

    ''' DISPLAY SALARY DETAILS OF EMPLOYEES IN MONTH '''
    salary_list = Salarymanage(db).get_all_emp_salary_data(companyname, salid)

    salary_status = db.collection(companyname).document('salary_status').get()
    salary_status = salary_status.get(datetime.date(1900, int(salid[4:]), 1).strftime('%B'))
    # print(salary_status)
    return render_template('salary_sheet_view.html', data=salary_list, salid=salid, companyname=companyname,
                           username=username, salary_status=salary_status)


@app.route('/<companyname>/<username>/salarysheetedit/<empid> <salid>', methods=['GET', 'POST'])
def salary_sheet_edit_(companyname, username, empid, salid):
    ''' EDIT SALARY DETAILS OF EMPLOYEE IN MONTH '''
    if request.method == 'POST':
        result = request.form
        Salarymanage(db).salary_update(companyname, empid, salid, data=result)
        return redirect(url_for('salary_sheet_view', salid=salid, companyname=companyname, username=username))

    holidays = db.collection(companyname).document('holidays').get().to_dict()
    moath_data = moth_count.count(holidays)
    working_days = moath_data['workingDays']
    employee_salary_data = Salarymanage(db).get_salary_data(companyname, empid, salid)
    salary_percentage = (db.collection(companyname).document('salary_calc').get()).to_dict()
    return render_template('salary_sheet_edit_personal.html', data=employee_salary_data, id=salid,
                           companyname=companyname, salary_data=salary_percentage, username=username,
                           working_days=working_days)


@app.route('/<companyname>/<username>/set_status/<salid>/<status>')
def set_status(companyname, username, salid, status):
    ''' SALARY SLIP PDF GENERATION '''
    month = datetime.date(1900, int(salid[3:]), 1).strftime('%B')
    status = status
    data = {month: status}
    salary_status = db.collection(companyname).document('salary_status').update(data)
    return redirect(url_for('salary_sheet_view', companyname=companyname, username=username, salid=salid))


@app.route('/<companyname>/<username>/pdf/<salid>')
def pdf(companyname, username, salid):
    ''' SALARY SLIP PDF GENERATION '''
    if 'storage_path' in session:
        path = session["storage_path"]
        salary = SalarySlip(db)
        salary.salary_slip(companyname, salid, path)
        return redirect(url_for('salary', companyname=companyname, username=username, salid=salid))


# @app.route('/<companyname>/<username>/excel/<salid>')
# def excel_for_bank(companyname,username, salid):
#     ''' GENERATE EXCELSHEET FOR BANK '''
#     if 'storage_path' in session:
#         path = session["storage_path"]
#         salary_excel = SalaryData(db)
#         salary_excel.add_data(companyname, salid, path)
#     return redirect(url_for('salary_sheet_view', salid=salid, companyname=companyname,username=username))


# @app.route('/<companyname>/tds/<id>', methods=['GET', 'POST'])
# def tds(companyname, id):
#     ''' DISPLAY TDS DETAILS OF EMPLOYEE '''
#     profile = Profile(companyname, db, id)
#     employee_tds_data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data()}
#     return render_template('tds_test.html', data=employee_tds_data, companyname=companyname)

@app.route('/<companyname>/<username>/add_data')
def testing(companyname, username):
    if 'excel_path' in session:
        excel_path = session['excel_path']
        print(excel_path)
        excel = ExcelData(db)
        excel.store_excel_data(companyname, excel_path)
        return redirect(url_for('dashboard', username=username, companyname=companyname))
    return render_template('add_excel_file.html', companyname=companyname, username=username)


@app.route('/<companyname>/<username>/send_email/<salid>')
def send_employee_salaryslip(companyname, username, salid):
    ''' GENERATE EXCELSHEET FOR BANK '''
    if 'storage_path' in session:
        path = session["storage_path"]
        auth_data = db.collection(companyname).document('admin').get().to_dict()
        company_mail = auth_data['AdminID']
        auth_password = auth_data['auth_password']
        docs = db.collection(companyname).document(u'employee').collection('employee').stream()
        employee_list = {}
        for doc in docs:
            employee_list.update({doc.id: doc.to_dict()})
        for key, value in employee_list.items():
            data = value
            mail_obj.send_employee_pdf(company_mail=company_mail, data=data, companyname=companyname,
                                       auth_password=auth_password, path=path)
    return redirect(url_for('salary_sheet_view', salid=salid, companyname=companyname, username=username))


if __name__ == '__main__':
    app.run(debug=True, port=300)
    # app.run(debug=True, host="192.168.0.150", port=3005)
