import concurrent.futures
from datetime import datetime

import executor as executor


class Dashboard():
    def __init__(self, db):
        self.db = db

    def _get_employee_data(self, emp_doc):
        employee_data = {'name': emp_doc.get('employeeName'),
                         'dob': emp_doc.get('dob'),
                         'doj': emp_doc.get('doj'),
                         'leaves': {}}
        if employee_data['dob']!='' or employee_data['dob']==None:
            dob = datetime.strptime(employee_data['dob'].strip(), '%Y-%m-%d')
            if dob.month == datetime.today().month:
                employee_data['birthday'] = employee_data['dob']
        if employee_data['doj'] != '':
            doj = datetime.strptime(employee_data['doj'], '%Y-%m-%d')
            if doj.month == datetime.today().month:
                years = datetime.today().year - doj.year
                employee_data['anniversary'] = {
                                                'name':employee_data['name'],
                                                'date': employee_data['doj'],
                                                'years': years}

        leaves = emp_doc.reference.collection('leaveMST')
        total_leaves = 0
        for leave in leaves.stream():
            if leave.id != 'total_leaves':
                dt2 = datetime.today().date()
                dt1 = datetime.strptime(leave.id, '%Y-%m-%d')
                diff = (dt2.year - dt1.year) * 12 + (dt2.month - dt1.month)
                if diff < 2:
                    employee_data['leaves'] = leave.get('fromdate')
            if leave.id != 'total_leaves':
                total_leaves += int(leave.get('days'))
        employee_data['total_leaves'] = total_leaves

        return employee_data

    def Dashboard_data(self, companyname):
        users_ref = self.db.collection(companyname).document('employee').collection('employee')
        employee_data = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for emp_doc in users_ref.stream():
                employee_data.append(executor.submit(self._get_employee_data, emp_doc))
        employee_on_leave, total_leaves, employee_birthday, employee_anniversary = {}, {}, {}, {}
        for future in concurrent.futures.as_completed(employee_data):
            result = future.result()
            if 'birthday' in result:
                employee_birthday[result['name']] = result['birthday']
            if 'anniversary' in result:
                employee_anniversary[result['name']] = result['anniversary']
            if result['leaves']:
                employee_on_leave[result['name']] = result['leaves']
            total_leaves[result['name']] = result['total_leaves']
        return employee_on_leave, total_leaves, employee_birthday, employee_anniversary


    def all_data(self, companyname):
        user_ref = self.db.collection(companyname).document(u'employee').collection('employee')
        all_employees = {
            'total_employees': int(len(user_ref.get())),
            'emp_on_probation': int(len(user_ref.where('designation', '==','Employee').get())),
            'emp_on_training': int(len(user_ref.where('designation', '==','Intern').get())) +
                               int(len(user_ref.where('designation', '==', 'Trainee').get()))
        }

        employee_overview = {
            'Internship': int(len(user_ref.where('designation', '==','Intern').get())),
            'Trainee': int(len(user_ref.where('designation', '==','Trainee').get())),
            'Employee': int(len(user_ref.where('designation', '==','Employee').get()))
        }

        exprience_list = {
            '0 to 1': int(len(user_ref.where('currentExperience','==','0 year').get())) +
                      int(len(user_ref.where('currentExperience', '==', '1 year').get())),
            '1 to 5': (int(len(user_ref.where('currentExperience', '==','2 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '3 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '4 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '5 year').get()))),
            '5 to 10': (int(len(user_ref.where('currentExperience', '==','6 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '7 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '8 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '9 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '10 year').get()))),
            'Above 10': (int(len(user_ref.where('currentExperience', '==','11 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '12 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '13 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '14 year').get()))) +
                      (int(len(user_ref.where('currentExperience', '==', '15 year').get())))
        }

        department = self.db.collection(companyname).document(u'department').get().to_dict()

        department_wise_emp = {}

        for dept in department:
            num_emp =  str(int(len(user_ref.where('department', '==', dept).get())))
            department_wise_emp.update({dept: num_emp})

        salary_wise_emp = {
            '0 to 20 K': int(len(user_ref.where('salary', '<', 20000).get())),
            '20 to 50 K': int(len(user_ref.where('salary', '<=', 50000).where('salary', '>', 20000).get())),
            '50 to 80 K': int(len(user_ref.where('salary', '<=', 80000).where('salary', '>', 50000).get())),
            '80 to 100 K': int(len(user_ref.where('salary', '<=', 100000).where('salary', '>', 80000).get())),
            '100 K +': int(len(user_ref.where('salary', '>', 100000).get()))
        }

        all_data_dashboard = {
            'all_employees': all_employees,
            'employee_overview': employee_overview,
            'exprience_list': exprience_list,
            'department': department,
            'department_wise_emp': department_wise_emp,
            'salary_wise_emp': salary_wise_emp
        }

        return all_data_dashboard



