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

        if datetime.strptime(employee_data['dob'], '%Y-%m-%d').month == datetime.today().month:
            employee_data['birthday'] = employee_data['dob']

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

    def Dashboard_data(self):
        users_ref = self.db.collection(u'alian_software').document('employee').collection('employee')
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


