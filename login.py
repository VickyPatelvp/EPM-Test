class Login():
    def __init__(self, db):
        self.db = db
        pass

    def login(self, data, comapyname):
        data_dict = {}
        for key, value in data.items():
            data_dict.update({key: value})
        docs = self.db.collection(comapyname).get()
        print(data_dict)
        if len(docs) > 0:
            docs = self.db.collection(comapyname).document('admin').get().to_dict()
            print('get obj')
            if len(docs)>0:
               print( docs['AdminID'],docs['password'])
               print(data_dict['email'],data_dict['password'])
               if (docs['AdminID'] == data_dict['email']) and str((docs['password']) == str(data_dict['password'])):
                   print('get_admin')
                   return 'Admin'
        doc = self.db.collection(comapyname).document("employee").collection('employee').where('email', "==",data_dict['email']).where('password', "==", str(data_dict['password'])).get()
        # docs = self.db.collection("alian_software").document("employee").collection('employee').where('email', "==", data_dict['email'] ).where('password',"==",str(data_dict['password'])).get()

        len(doc)
        # print(doc)
        if len(doc) > 0:
            for d in doc:
                print(d.to_dict())
            if doc[0].to_dict()['department']=='HR':
                return {"name":doc[0].to_dict()['employeeName'],"type":'HR'}
            else:
                return {"name":doc[0].to_dict()['employeeName'],"type":'Employee',"empid":doc[0].to_dict()['userID']}
        return False