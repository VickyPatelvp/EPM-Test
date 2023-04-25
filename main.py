import datetime
import re


from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from flask import Flask, render_template, request, redirect, url_for
from firebase_admin import credentials
from firebase_admin import firestore

from leave_manage import Leavemanage
from details import Profile
from create_new_employee import result
from salary_manage import Salarymanage
from department import Department
from update_employee import Update_information
from dashboard import Dashboard
from tds_data import TDSData
from excel_sheet import SalaryData
from register import Register
from login import Login
# FLASK APP
app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# USE A SERVICE ACCOUNT

cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
db = firestore.client()

leavobj = Leavemanage(db)
dept=Department(db)
update_obj=Update_information(db)
dashboard_obj=Dashboard(db)
register_obj=Register(db)
login_obj=Login(db)

if datetime.date.today().day==1:
     pass
#     Code

# Leave reset
if datetime.date.today().day==1 or datetime.date.month==1:
    leavobj.leave_add()


@app.route('/login', methods=["POST", "GET"])
def login():
    responce=''
    if request.method == 'POST':
        data = request.form
        responce = login_obj.login(data)
        if responce==True:
            return redirect(url_for('dashboard'))
    ''' LOGIN PAGE '''
    return render_template('login.html',responce=responce)


@app.route('/register',methods=["POST", "GET"] )
def register():

    responce=''
    if request.method=='POST':
        data=request.form
        responce=register_obj.register(data)
        if responce==True:
            return redirect(url_for('login'))

    ''' REGISTER PAGE '''
    return render_template('register.html',responce=responce)

@app.route('/')
def dashboard():

    ''' DISPLAY DASHBOARD '''

    employee_on_leave,total_leaves,employee_birthday, employee_anniversary = dashboard_obj.Dashboard_data()
    return render_template('dashboard.html',employee_on_leave=employee_on_leave,total_leaves=total_leaves,employee_birthday=employee_birthday,employee_anniversary=employee_anniversary)




@app.route('/employeelist', methods=['GET', 'POST'])
def employee_list():

    ''' DISPLAY LIST OF EMPLOYEES IN COMPANY '''

    def get_employee_data():
        docs = db.collection(u'alian_software').document(u'employee').collection('employee').stream()
        employee_list = {}
        for doc in docs:
            employee_list.update({doc.id: doc.to_dict()})
        return employee_list

    def get_department_data():
        department = (db.collection(u'alian_software').document(u'department').get()).to_dict()
        return department

    with concurrent.futures.ThreadPoolExecutor() as executor:
        employee_data = executor.submit(get_employee_data)
        department_data = executor.submit(get_department_data)

    employee_list = employee_data.result()
    department = department_data.result()
    return render_template('employees_list.html', data=employee_list, department=department)


@app.route('/result', methods=['POST', 'GET'])
def add():
    ''' NEW EMPLOYEE DATA STORE IN DATABASE AND DISPLAY IN LIST '''
    result()
    # session["j"] = True
    return redirect(url_for('employee_list'))


@app.route('/employeeprofile/<id>', methods=['GET', 'POST'])
def employee_profile(id):
    ''' DISPLAY EMPLOYEE DETAILS '''
    users_ref = db.collection(u'alian_software').document('employee').collection('employee').document(id).collection(
        'leaveMST')
    if request.method == 'POST':
        ''' Store leave Data '''
        result = request.form

        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(leavobj.take_leave, users_ref, data=result)

    ''' GET LEAVE DATA '''
    with ThreadPoolExecutor(max_workers=2) as executor:
        total_leave_future = executor.submit(leavobj.get_total_leave, users_ref)
        leave_list_future = executor.submit(leavobj.leave_list, users_ref)

    total_leave = total_leave_future.result()
    leave_list = leave_list_future.result()

    ''' GET EMPLOYEE DATA '''
    with ThreadPoolExecutor(max_workers=2) as executor:
        personal_data_future = executor.submit(Profile(id).personal_data)
        tds_data_future = executor.submit(Profile(id).tds_data)
        salary_data_future = executor.submit(Profile(id).salary_data)

    data = {'personal_data': personal_data_future.result(), 'tds_data': tds_data_future.result(),
            'salary_data': salary_data_future.result()}
    leave_status = True
    return render_template('employee_profile.html', leave=leave_status, data=data, total_leave=total_leave,
                           leave_list=leave_list)


@app.route('/employeeprofileedit/<id>', methods=['GET', 'POST'])
def employee_profile_edit(id):
    ''' DISPLAY EMPLOYEE DETAILS '''
    users_ref = db.collection(u'alian_software').document('employee').collection('employee').document(id).collection(
        'leaveMST')

    if request.method == 'POST':
        ''' Store leave Data '''
        result = request.get_json()

        # print(result)

        leavobj.take_leave_edit(users_ref, data=result)

    ''' GET LEAVE DATA '''
    total_leave = leavobj.get_total_leave(users_ref)
    leave_list = leavobj.leave_list(users_ref)

    ''' EDIT EMPLOYEE DETAILS '''
    profile = Profile(id)
    data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data(), 'salary_data': profile.salary_data()}
    return render_template('employee_profile_edit.html', data=data,total_leave=total_leave,leave_list=leave_list)


''' UPDATE EMPLOYEE PERSONAL DETAILS '''
@app.route('/personal_data_update/<id>', methods=['GET', 'POST'])
def personal_data_update(id):
    if request.method=='POST':
        print('hello1')
        form = request.get_json()
        update_obj.update_personal_info(form,id)
        print('hello1')

    return redirect(url_for('employee_profile_edit',id=id))


''' UPDATE EMPLOYEE TDS DETAILS '''
@app.route('/tds_data_update/<id>', methods=['GET', 'POST'])
def tds_data_update(id):
    if request.method=='POST':
        print('hello1')
        form=request.get_json()

        update_obj.update_tds_info(form, id)

        print('hello1')
    return redirect(url_for('employee_profile_edit', id=id))


''' DISPLAY DEPARTMENT '''
@app.route('/department', methods=['GET', 'POST'])
def department():
    ''' DISPLAY DEPARTMENT '''
    if request.method == 'POST':
        ''' Add New DEPARTMENT '''
        result=request.form
        dept.add_deaprtment(result)

    doc_ref = db.collection(u'alian_software').document(u'department')
    data = doc_ref.get().to_dict()
    return render_template('department.html', data=data, obj=dept)


@app.route('/delete_department/<dep> <pos>', methods=['GET', 'POST'])
def delete_department(dep,pos):
    a=dep,pos
    pattern = r'[^a-zA-Z\d\s]'
    # Use the re.sub() function to replace all occurrences of the pattern with an empty string
    dep = re.sub(pattern, '', dep)
    pos=re.sub(pattern,'',pos)
    dept.delete_deaprtment(dep,pos)
    return redirect(url_for('department'))

@app.route('/delete_department/<dep> <pos>', methods=['GET', 'POST'])
def edit_department(dep, pos):
    a=dep,pos
    pattern = r'[^a-zA-Z\d\s]'
    # Use the re.sub() function to replace all occurrences of the pattern with an empty string
    dep = re.sub(pattern, '', dep)
    pos=re.sub(pattern,'',pos)
    dept.delete_deaprtment(dep,pos)
    return redirect(url_for('department'))



@app.route('/my-route')
def my_route():
    return dept


@app.route('/salary', methods=['GET', 'POST'])
def salary():
    ''' DISPLAY SALARY DETAILS OF ALL MONTH IN YEAR '''
    salary_list = Salarymanage(db).get_all_month_salary_data()
    return render_template('salary_sheet_month.html',data=salary_list)

@app.route('/salarysheetview/<salid>', methods=['GET', 'POST'])
def salary_sheet_view(salid):
    ''' DISPLAY SALARY DETAILS OF EMPLOYEES IN MONTH '''
    salary_list= Salarymanage(db).get_all_emp_salary_data(salid)
    return render_template('salary_sheet_view.html', data=salary_list,salid=salid)

@app.route('/salarysheetedit', methods=['GET', 'POST'])
def salary_sheet_edit():

    ''' EDIT SALARY DETAILS OF ALL EMPLOYEES IN MONTH '''
    docs = db.collection(u'alian_software').document(u'employee').collection('employee').stream()
    employee_list = {}
    for doc in docs:
        employee_list.update({doc.id: doc.to_dict()})
    return render_template('salary_sheet_edit_all.html', data=employee_list)

@app.route('/salarysheetedit/<empid> <salid>', methods=['GET', 'POST'])
def salary_sheet_edit_(empid,salid):
    if request.method=='POST':
        result = request.form
        Salarymanage(db).salary_update(empid, salid,data=result)
        return redirect(url_for('salary_sheet_view',salid=salid))

    ''' EDIT SALARY DETAILS OF PARTICULAR EMPLOYEES IN MONTH '''
    employee_salary_data = Salarymanage(db).get_salary_data(empid,salid)
    return render_template('salary_sheet_edit_personal.html',data=employee_salary_data ,id=salid)

@app.route('/tds/<id>', methods=['GET', 'POST'])
def tds(id):
    ''' DISPLAY SALARY DETAILS OF ALL MONTH IN YEAR '''
    profile = Profile(id)
    employee_tds_data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data()}
    return render_template('tds_test.html', data=employee_tds_data)

if datetime.date.today().day==20:
    # TDS Data

    TDSData(db).deduction("EMP002")


    # Create Excel-sheet for Bank

    SalaryData(db).add_data("EMP002")

if __name__ == '__main__':
    app.run(debug=True, port=300)

# app.run(debug=True, host="192.168.0.53", port=3005)
