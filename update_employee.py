class Upate_information():
    def __init__(self,db):
       self.db=db
    def update_personal_info(self,data,id):
        data_dict ={}
        for key, value in data.items():
            if value != '':
                data_dict.update({key: value})
        a = self.db.collection(u'alian_software').document('employee').collection('employee').document(id).update(data_dict)
        print(a)
    def update_tds_info(self, data, id):
        data_dict = {}
        for key, value in data.items():
            if value != '':
                data_dict.update({key: value})
        print(data_dict)
        a=self.db.collection(u'alian_software').document('employee').collection('employee').document(id).collection(
            'tdsmst').document('tds').update(data_dict)
        print(a)