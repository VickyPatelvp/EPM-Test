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
        docs = self.db.collection(data_dict['companyname']).get()
        if len(docs) > 0:
            print('Already Company Registered')
            return 'Already Company Registered'
        else:
            self.db.collection(data_dict['companyname']).document('Admin').set(data_dict)
            '''SEND ID PASS WORD MAIL'''
            self.mail.register_responce_mail(companyname=data_dict['companyname'])
            return True
