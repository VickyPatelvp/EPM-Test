from flask import Flask, render_template, request, redirect, url_for
from leave_manage import Leavemanage
from firebase_admin import credentials
from firebase_admin import firestore
from details import Profile
from create_new_employee import result
from salary_manage import Salarymanage

# FLASK APP
app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# USE A SERVICE ACCOUNT

cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')

db = firestore.client()

leavobj = Leavemanage(db)

@app.route('/', methods=["POST", "GET"])
def login():

    ''' LOGIN PAGE '''

    return render_template('login.html')


@app.route('/register')
def register():

    ''' REGISTER PAGE '''

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():

    ''' DISPLAY DASHBOARD '''

    return render_template('dashboard.html')


@app.route('/employeelist', methods=['GET', 'POST'])
def employee_list():
    ''' DISPLAY LIST OF EMPLOYEES IN COMPANY '''
    docs = db.collection(u'alian_software').document(u'employee').collection('employee').stream()
    employee_list = {}
    for doc in docs:
        employee_list.update({doc.id: doc.to_dict()})
    return render_template('employees_list.html', data=employee_list)



# @app.route('/result', methods=['POST', 'GET'])
# def add():
#     ''' NEW EMPLOYEE DATA STORE IN DATABASE AND DISPLAY IN LIST '''
#     result()
#     # session["j"] = True
#     # return redirect(url_for('employee_list', session=session["j"]))


@app.route('/employeeprofile/<id>', methods=['GET', 'POST'])
def employee_profile(id):
    ''' DISPLAY EMPLOYEE DETAILS '''
    users_ref = db.collection(u'alian_software').document('employee').collection('employee').document(id).collection('leaveMST')
    if request.method=='POST':
        ''' Store leave Data '''
        result=request.form
        leavobj.take_leave(users_ref,data= result)

    ''' GET LEAVE DATA '''
    total_leave = leavobj.get_total_leave(users_ref)
    leave_list = leavobj.leave_list(users_ref)

    ''' GET EMPLOYEE DATA '''
    profile = Profile(id)
    data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data(),'salary_data': profile.salary_data()}
    leave_status = True
    return render_template('employee_profile.html', leave=leave_status, data=data,total_leave=total_leave,leave_list=leave_list)



@app.route('/employeeprofileedit/<id>', methods=['GET', 'POST'])
def employee_profile_edit(id):
    ''' DISPLAY EMPLOYEE DETAILS '''
    users_ref = db.collection(u'alian_software').document('employee').collection('employee').document(id).collection(
        'leaveMST')
    if request.method == 'POST':
        ''' Store leave Data '''
        result = request.form
        leavobj.take_leave(users_ref, data=result)

    ''' GET LEAVE DATA '''
    total_leave = leavobj.get_total_leave(users_ref)
    leave_list = leavobj.leave_list(users_ref)

    ''' EDIT EMPLOYEE DETAILS '''
    profile = Profile(id)
    data = {'personal_data': profile.personal_data(), 'tds_data': profile.tds_data(),
            'leave_data': profile.leave_data(), 'salary_data': profile.salary_data()}
    return render_template('employee_profile_edit.html', data=data,total_leave=total_leave,leave_list=leave_list)



@app.route('/department', methods=['GET', 'POST'])
def department():
    ''' DISPLAY DEPARTMENT '''
    department_data = Profile.department_data(self=db)
    return render_template('department.html', data=department_data)

@app.route('/salary', methods=['GET', 'POST'])
def salary():
    ''' DISPLAY SALARY DETAILS OF ALL MONTH IN YEAR '''
    return render_template('salary_sheet_month.html')


@app.route('/salarysheetview', methods=['GET', 'POST'])
def salary_sheet_view():
    ''' DISPLAY SALARY DETAILS OF EMPLOYEES IN MONTH '''
    salary_list= Salarymanage(db).get_all_emp_salary_data()
    return render_template('salary_sheet_view.html', data=salary_list)


@app.route('/salarysheetedit', methods=['GET', 'POST'])
def salary_sheet_edit():

    ''' EDIT SALARY DETAILS OF ALL EMPLOYEES IN MONTH '''
    docs = db.collection(u'alian_software').document(u'employee').collection('employee').stream()
    employee_list = {}
    for doc in docs:
        employee_list.update({doc.id: doc.to_dict()})
    return render_template('salary_sheet_edit_all.html', data=employee_list)


@app.route('/salarysheetedit/<id>', methods=['GET', 'POST'])
def salary_sheet_edit_(id):

    ''' EDIT SALARY DETAILS OF PARTICULAR EMPLOYEES IN MONTH '''
    profile = Profile(id)
    employee_data = {'personal_data': profile.personal_data(), 'salary_data': profile.salary_data()}
    return render_template('salary_sheet_edit_personal.html', data=employee_data)


if __name__ == '__main__':
    app.run(debug=True, port=3005)

# app.run(debug=True, host="192.168.0.53", port=3005)
