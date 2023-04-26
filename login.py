class Login():
    def __init__(self,db):
        self.db=db
        pass

    def login(self,data,comapyname):
        data_dict = {}
        for key, value in data.items():
            data_dict.update({key: value})
        docs = self.db.collection(comapyname).get()
        if len(docs) > 0:
            docs = self.db.collection(comapyname).document('Admin').get().to_dict()
            if docs['email']==data_dict['email'] and docs['password']==data_dict['password']:
                return True
            else:
                return 'Invalid Id passoword'
        else:
            return 'Invalid Company Name'
