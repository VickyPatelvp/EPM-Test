from firebase_admin import firestore
import firebase_admin

from firebase_admin import credentials
cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()



class Department:
    def __init__(self,db):
        self.db=db
    def add_deaprtment(self,result):
        doc_ref = self.db.collection(u'alian_software').document(u'department')
        print(doc_ref)
        for key, value in doc_ref.get().to_dict().items():
               if key=="HR":
                   doc_ref.update({f'{key}.{result}':35000})



        #     if key == 'deptname':
        #         deptnm = value
        #     elif re.findall("^pos", key):
        #         pos.append(value)
        #     elif re.findall("^sal", key):
        #         sal.append(value)
        # for i in range(len(pos)):
        #     data.update({pos[i]: sal[i]})
        # doc_ref.update({deptnm: data})
        # if result == doc_ref:
        #     doc_ref = self.db.collection(u'alian_software').document(u'department')
        # doc_ref =self.db.collection(u'alian_software').document(u'department')
        # pos = []
        # sal = []
        # data = {}
        deptnm = ''
        # for key, value in result.items():
        #     if key == 'deptname':
        #         deptnm = value
        #     elif re.findall("^pos", key):
        #         pos.append(value)
        #     elif re.findall("^sal", key):
        #         sal.append(value)
        # for i in range(len(pos)):
        #     data.update({pos[i]: sal[i]})
        # doc_ref.update({deptnm: data})

    def delete_deaprtment(self,dept,pos):
        doc_ref = self.db.collection(u'alian_software').document(u'department')
        position=dept+'.'+pos
        doc_ref.update({
            position: firestore.DELETE_FIELD
        })

    def edit_department(self,dept,pos):
        doc_ref = self.db.collection(u'alian_software').document(u'department').get()
        data=doc_ref.get(dept)
        data=data.get(pos)
        print(data)
        return data
obj=Department(db)

obj.add_deaprtment("HR2")