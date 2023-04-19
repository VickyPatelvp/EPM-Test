import re
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')

db = firestore.client()


class Department:
    def __init__(self,db):
        self.db=db
    def add_deaprtment(self,result):
        doc_ref =self.db.collection(u'alian_software').document(u'department')
        pos = []
        sal = []
        data = {}
        deptnm = ''
        for key, value in result.items():
            if key == 'deptname':
                deptnm = value
            elif re.findall("^pos", key):
                pos.append(value)
            elif re.findall("^sal", key):
                sal.append(value)
        for i in range(len(pos)):
            data.update({pos[i]: sal[i]})
        doc_ref.update({deptnm: data})

    def delete_deaprtment(self,dept,pos):
        doc_ref = self.db.collection(u'alian_software').document(u'department')
        position=dept+'.'+pos
        doc_ref.update({
            position: firestore.DELETE_FIELD
        })

    def edit_department(self,dept,pos,sal ):
        doc_ref = self.db.collection(u'alian_software').document(u'department')

        doc_ref.update({
            'my_map_field.my_subfield': 'new_value'
        })

# fields_to_delete = {
#     'field1': firestore.DELETE_FIELD,
#     'field2': firestore.DELETE_FIELD,
#     # add more fields here if needed
# }