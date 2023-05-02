from mail import Mail


class Register():
    def __init__(self, db):
        self.db = db
        self.mail = Mail()

    def register(self, data=None):
        data_dict = {}
        for key, value in data.items():
            data_dict.update({key: value})
        print(data_dict)
        docs = self.db.collection(data_dict['CompanyName']).get()
        if len(docs) > 0:
            print('Already Company Registered')
            return 'Already Company Registered'
        else:
            self.db.collection(data_dict['CompanyName']).document('admin').set(data_dict)
            self.db.collection(data_dict['CompanyName']).document('department').set({})
            self.db.collection(data_dict['CompanyName']).document('employee').set({})
            self.db.collection(data_dict['CompanyName']).document('month_data').set({})
            self.db.collection(data_dict['CompanyName']).document('holiday').set({})
            self.db.collection(data_dict['CompanyName']).document('salary_calc').set({})

            '''SEND ID PASS WORD MAIL'''
            self.mail.register_responce_mail(companyname=data_dict['CompanyName'])
            return True
