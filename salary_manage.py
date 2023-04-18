import datetime


class Salarymanage():
    def __init__(self,db):
        self.db=db

    def salary_update(self,ref_obj,data=None):
        data_dict = {}
        print('hello')
        for key, value in data.items():
            data_dict.update({key: value})
        id='sal00' + str(datetime.date.today().month)
        ref_obj.document(id).set(data_dict)
        # ref_obj.document()

    def get_all_emp_salary_data(self):
        docs = self.db.collection(u'alian_software').document(u'employee').collection('employee').stream()
        salary_list = {}
        for doc in docs:
            # salary_list.update(doc.id[])
            print(type(doc.id))
            print(doc.id)
            print(doc.to_dict()['employeeName'])
            salary_list.update(
                {doc.id: {'employeeName':doc.to_dict()['employeeName']}})
            print(salary_list)
            salary_data=self.db.collection(u'alian_software').document(u'employee').collection('employee').document(str(doc.id)).collection('salaryslips').stream()
            for docs in salary_data:
                salary_list.update({doc.id:docs.get().to_string()})


        print(salary_list)
        # return salary_list