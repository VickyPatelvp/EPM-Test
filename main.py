import datetime
# datetime.date.strftime()
import time
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, render_template, request, redirect, url_for, session

import mail
from leave_manage import Leavemanage
from firebase_admin import credentials, storage
from firebase_admin import firestore
from details import Profile
from create_new_employee import Create
from salary_manage import Salarymanage
from department import Department
from update_employee import Update_information
from dashboard import Dashboard
import re
from tds_data import TDSData
from excel_sheet import SalaryData
import concurrent.futures
from salary_slip import SalarySlip
from register import Register
from login import Login
from moth_days import Month_count
from mail import Mail

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
mail_obj=Mail()

@app.route('/<comapyname>/login', methods=["POST", "GET"])
def login(comapyname):
    responce = ''
    if request.method == 'POST':
        data = request.form
        responce = login_obj.login(data, comapyname)
        print(data)
        if responce == 'Admin':
            # session['companyname']=comapyname
            return redirect(url_for('dashboard', companyname=comapyname,username=responce))
        elif responce !=False:
            if responce['type']=='HR':
                return redirect(url_for('dashboard', companyname=comapyname, username=responce['name']))
            else:
                 return redirect(url_for('employee_profile', companyname=comapyname, username=responce['name'],id=responce['empid']))
        else:
            responce ='Inavalid Id and Password'
    ''' LOGIN PAGE '''
    url = f'/{comapyname}/login'
    return render_template('login.html', responce=responce, url=url)


@app.route('/success', methods=["POST", "GET"])
def success():
    return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def register():
    responce = ''
    if request.method == 'POST':
        data=request.form
        responce=register_obj.register(data)
        if responce == True:
            return redirect(url_for('success'))

    ''' REGISTER PAGE '''
    return render_template('register.html',responce=responce)


if datetime.date.today().day == 27:
    # TDS Data
    TDSData(db).deduction("EMP002")


@app.route('/<companyname>/<username>/dashboard', methods=['GET', 'POST'])
def dashboard(companyname,username):

    if request.method == 'POST':
        form = request.form.to_dict()
        # print(form)
        data={ str(form["date"]):form["description"]}
        db.collection(companyname).document('holidays').update(data)
        holidays = db.collection(companyname).document('holidays').get().to_dict()

        moath_data = moth_count.count(holidays)
        db.collection(companyname).document('month_data').set(moath_data)

    # Leave reset
    if datetime.date.today().day == 1 or datetime.date.month == 1:
        leaveobj.leave_add(companyname)

    ''' DISPLAY DASHBOARD '''

    holidays = db.collection(companyname).document('holidays').get().to_dict()
    moath_data = moth_count.count(holidays)
    holidays=moth_count.get_holidays(holidays)
    employee_on_leave, total_leaves, employee_birthday, employee_anniversary = dashboard_obj.Dashboard_data(companyname)
    return render_template('dashboard.html', employee_on_leave=employee_on_leave, total_leaves=total_leaves,
                           employee_birthday=employee_birthday, employee_anniversary=employee_anniversary,
                           moath_data=moath_data, companyname=companyname,holidays=holidays,username=username)


@app.route('/<companyname>/<username>/employeelist', methods=['GET', 'POST'])
def employee_list(companyname ,username):
    print(username)
    if request.method == 'POST':
        employee_mail = request.form.get('new_email')
        print(employee_mail)
        mail_obj.new_employee_mail(employee_mail,companyname)
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
    return render_template('employees_list.html', data=employee_list, department=department, companyname=companyname,username=username)


@app.route('/<companyname>/<username>/result', methods=['POST', 'GET'])
def add(companyname, username):
    ''' NEW EMPLOYEE DATA STORE IN DATABASE AND DISPLAY IN LIST '''
    create = Create(db, companyname)
    create.result()
    return redirect(url_for('employee_list', companyname=companyname , username=username))


@app.route('/<companyname>/register_employee', methods=['POST', 'GET'])
def employee_register_by_mail(companyname):
    if request.method=='POST':
        create = Create(db, companyname)
        create.result()
        email=request.form.get('email')
        mail_obj.employee_registered_mail(email=email,companyname=companyname)
        return redirect(url_for('success'))

    def get_department_data():
        department = (db.collection(companyname).document(u'department').get()).to_dict()
        return department
    with concurrent.futures.ThreadPoolExecutor() as executor:
        department_data = executor.submit(get_department_data)
    department=get_department_data()
    return render_template('add_employee.html',companyname=companyname,department=department,department_data=department_data)

@app.route('/<companyname>/<username>/employeeprofile/<id>', methods=['GET', 'POST'])
def employee_profile(companyname,username, id):
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
        personal_data_future = executor.submit(Profile( db, id,companyname).personal_data)
        tds_data_future = executor.submit(Profile(db, id, companyname ).tds_data)
        salary_data_future = executor.submit(Profile(db, id, companyname).salary_data)

    data = {'personal_data': personal_data_future.result(), 'tds_data': tds_data_future.result(),
            'salary_data': salary_data_future.result()}

    leave_status=False
    leave_status_date=''
    for i in leave_list :
        if i != 'total_leaves' :
          leave_date=(datetime.datetime.strptime(leave_list[i]['applydate'],'%Y-%m-%d').month)
          if leave_date== datetime.datetime.today().month:
              leave_status = True
              leave_status_date=(f'{leave_list[i]["fromdate"]} to {leave_list[i]["todate"]} ')


    return render_template('employee_profile.html', leave=leave_status, data=data, total_leave=total_leave,
                           leave_list=leave_list, companyname=companyname,leave_date=leave_status_date ,username=username)


@app.route('/<companyname>/<username>/personal_data_update/<id>', methods=['GET', 'POST'])
def personal_data_update(companyname,username, id):
    ''' UPDATE EMPLOYEE PERSONAL DETAILS '''
    if request.method == 'POST':
        form = request.get_json()
        update_obj.update_personal_info(companyname, form, id)
        return redirect(url_for('employee_profile', id=id, companyname=companyname ,username=username))

@app.route('/<companyname>/<username>/tds_data_update/<id>', methods=['GET', 'POST'])
def tds_data_update(companyname,username, id):
    ''' UPDATE EMPLOYEE TDS DETAILS '''
    if request.method == 'POST':
        form = request.get_json()
        update_obj.update_tds_info(companyname, form, id)
    return redirect(url_for('employee_profile', id=id, companyname=companyname,username=username))


@app.route('/<companyname>/<username>/department', methods=['GET', 'POST'])
def department(companyname, username):
    ''' DISPLAY DEPARTMENT '''
    if request.method == 'POST':
        ''' Add New DEPARTMENT '''
        result = request.form
        print(result)
        dept.add_department(companyname, result)
    doc_ref = db.collection(str(companyname)).document(u'department')
    data = doc_ref.get().to_dict()
    return render_template('department.html', data=data, obj=dept, companyname=companyname, username=username)

@app.route('/<companyname>/<username>/delete_department/<dep> <pos>', methods=['GET', 'POST'])
def delete_department(companyname,username, dep, pos):
    ''' DELETE DEPARTMENT '''
    a = dep, pos
    pattern = r'[^a-zA-Z\d\s]'
    # Use the re.sub() function to replace all occurrences of the pattern with an empty string
    dep = re.sub(pattern, '', dep)
    pos = re.sub(pattern, '', pos)
    dept.delete_department(companyname, dep, pos)
    return redirect(url_for('department', companyname=companyname ,username=username))





@app.route('/my-route')
def my_route():
    return dept


@app.route('/<companyname>/<username>/salary', methods=['GET', 'POST'])
def salary(companyname,username):
    ''' DISPLAY SALARY DETAILS OF ALL MONTH IN YEAR '''

    if request.method == 'POST':
        form = request.form
        data_dict = {}
        for key, value in form.items():
            if value !='':
                data_dict.update({key: value})
        # ADD Salary Criteria
        docs=db.collection(companyname).document('salary_calc')

        if len(docs.get().to_dict())==0:
            db.collection(companyname).document('salary_calc').set(data_dict)
        else:
            db.collection(companyname).document('salary_calc').update(data_dict)
    salary_criteria = db.collection(str(companyname)).document('salary_calc').get().to_dict()
    salary_list = Salarymanage(db).get_all_month_salary_data(companyname)
    return render_template('salary_sheet_month.html', data=salary_list, salary_criteria=salary_criteria,
                           companyname=companyname ,username=username)


@app.route('/<companyname>/<username>/salarysheetview/<salid>', methods=['GET', 'POST'])
def salary_sheet_view(companyname, username, salid):
    # month = int(salid[5:])
    ''' DISPLAY SALARY DETAILS OF EMPLOYEES IN MONTH '''
    salary_list = Salarymanage(db).get_all_emp_salary_data(companyname, salid)
    return render_template('salary_sheet_view.html', data=salary_list, salid=salid, companyname=companyname ,username=username)



@app.route('/<companyname>/<username>/salarysheetedit/<empid> <salid>', methods=['GET', 'POST'])
def salary_sheet_edit_(companyname, username, empid, salid):
    ''' EDIT SALARY DETAILS OF EMPLOYEE IN MONTH '''
    if request.method == 'POST':
        result = request.form
        Salarymanage(db).salary_update(companyname, empid, salid, data=result)
        return redirect(url_for('salary_sheet_view', salid=salid, companyname=companyname,username=username ))

    employee_salary_data = Salarymanage(db).get_salary_data(companyname, empid, salid)
    return render_template('salary_sheet_edit_personal.html', data=employee_salary_data, id=salid,
                           companyname=companyname ,username=username)


@app.route('/<companyname>/<username>/pdf/<salid>')
def pdf(companyname, username,salid):
    ''' SALARY SLIP PDF GENERATION '''
    salary = SalarySlip(db)
    salary.salary_slip(companyname, salid)
    return redirect(url_for('salary', companyname=companyname,username=username,salid=salid))


@app.route('/<companyname>/excel/<salid>')
def excel_for_bank(companyname, salid):
    ''' GENERATE EXCELSHEET FOR BANK '''
    salary_excel = SalaryData(db)
    salary_excel.add_data(companyname, salid)
    return redirect(url_for('salary_sheet_view', salid=salid, companyname=companyname))


@app.route('/<companyname>/tds/<id>', methods=['GET', 'POST'])
def tds(companyname, id):
    ''' DISPLAY TDS DETAILS OF EMPLOYEE '''
    profile = Profile(companyname, db, id)
    employee_tds_data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data()}
    return render_template('tds_test.html', data=employee_tds_data, companyname=companyname)


# @app.route('/test_create')
# def test():
#     def get_department_data():
#         department = (db.collection(u'alian_software').document(u'department').get()).to_dict()
#         return department
#
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         department_data = executor.submit(get_department_data)
#
#     department = department_data.result()
#     return render_template('create.html', department=department)


if __name__ == '__main__':
    app.run(debug=True, port=300)
    # app.run(debug=True, host="192.168.0.150", port=3005)
