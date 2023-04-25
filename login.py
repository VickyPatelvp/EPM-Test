class Login():
    def __init__(self,db):
        self.db=db
        pass

    def login(self,data):
        data_dict = {}
        for key, value in data.items():
            data_dict.update({key: value})
        docs = self.db.collection(data_dict['companyname']).get()
        if len(docs) > 0:
            docs = self.db.collection(data_dict['companyname']).document('Admin').get().to_dict()
            if docs['email']==data_dict['email'] and docs['password']==data_dict['password']:
                return True
            else:
                return 'Invalid Id passoword'
        else:
            return 'Invalid Company Name'
