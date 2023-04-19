import datetime


class Salarymanage():
    def __init__(self,db):
        self.db=db

    # def salary_create(self,empid,salid,data=None):
    #     all_employees=self.db.collection(u'alian_software').document('employee').collection('employee').stream()
    #     for empi in all_employees:
    #
    #      data_dict = {}
    #     for key, value in data.items():
    #         data_dict.update({key: value})
    #     id='sal00' + str(datetime.date.today().month)
    #     a = self.db.collection(u'alian_software').document('employee').collection('employee').document(
    #         empid).collection(
    #         'salaryslips').document(salid).update(data_dict)
    #     # ref_obj.document()

    def salary_update(self,empid,salid,data=None):
        data_dict = {}
        for key, value in data.items():
            data_dict.update({key: value})
        a=self.db.collection(u'alian_software').document('employee').collection('employee').document(empid).collection(
            'salaryslips').document(salid).update(data_dict)

    def get_all_month_salary_data(self):
        docs = self.db.collection(u'alian_software').document(u'employee').collection('employee').stream()
        employee_salary = {}


        for emp in docs:
            salary_list = {}
            salary_data=self.db.collection(u'alian_software').document(u'employee').collection('employee').document(str(emp.id)).collection('salaryslips').stream()
            for doc in salary_data:
                salary_list.update({doc.id: doc.to_dict()})
            employee_salary.update({emp.id:salary_list})

        salary_data = {}
        for i in employee_salary:
            for j in employee_salary[i]:
                if j == "salid":
                    continue
                if j not in salary_data.keys():
                    salary_data.update({j: {
                        'netSalary': 0,
                        'grossSalary': 0,
                        'epfo': 0,
                        'pt': 0,
                        'tds': 0,
                    }})
                if j != "salid":
                    salary_data.update({j: {
                        'netSalary': salary_data[j]['netSalary'] + int(employee_salary[i][j]["netSalary"]),
                        'grossSalary': salary_data[j]['grossSalary'] +int (employee_salary[i][j]["grossSalary"]),
                        'epfo': salary_data[j]['epfo'] + int(employee_salary[i][j]["epfo"]),
                        'pt': salary_data[j]['pt'] + int(employee_salary[i][j]["pt"]),
                        'tds': salary_data[j]['tds'] + int(employee_salary[i][j]["tds"]),
                    }})

        return salary_data


    def get_all_emp_salary_data(self,month):
        docs = self.db.collection(u'alian_software').document(u'employee').collection('employee').stream()
        employee_salary = {}
        for emp in docs:
            salary_list = {}
            salary_data=self.db.collection(u'alian_software').document(u'employee').collection('employee').document(str(emp.id)).collection('salaryslips').document(month).get().to_dict()
            if salary_data != None:
                employee_salary.update({emp.id:salary_data})
        return employee_salary

    def get_salary_data(self,empid,salid):
        doc = users_ref = self.db.collection(u'alian_software').document('employee').collection('employee').document(empid).collection('salaryslips').document(salid).get()
        data_dict = {}
        data_dict.update({doc.id: doc.to_dict()})
        return data_dict
