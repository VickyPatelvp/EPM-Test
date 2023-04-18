from firebase_admin import firestore
import firebase_admin

from firebase_admin import credentials
cred = credentials.Certificate('employee-payroll-system-848cc-firebase-adminsdk-xkv2w-cfaf2643db.json')
firebase_app = firebase_admin.initialize_app(cred)

db = firestore.client()


class Profile:

    # GETTING ID
    def __init__(self, id):
        self.db = db
        self.id = id

    # PERSONAL DATA
    def personal_data(self):
        users_ref = db.collection(u'alian_software').document(u'employee').collection('employee').document(
            str(self.id)).get()
        return users_ref.to_dict()

    # TDS DATA
    def tds_data(self):
        user_ref = db.collection(u'alian_software').document(u'employee').collection('employee').document(
            str(self.id)).collection('tdsmst').document('tds').get()
        print(user_ref.to_dict())
        return user_ref.to_dict()

    # LEAVE DATA
    def leave_data(self):
        data = []
        user_ref = db.collection(u'alian_software').document(u'employee').collection('employee').document(
            str(self.id)).collection('leaveMST').document('date').get()
        data.append(user_ref.to_dict())
        user_ref = db.collection(u'alian_software').document(u'employee').collection('employee').document(
            str(self.id)).collection('leaveMST').document('total_leaves').get()
        data.append(user_ref.to_dict())
        return data

    # DEPARTMENT DATA
    def department_data(self):
        user_ref = db.collection(u'alian_software').document(u'department').get()
        return user_ref.to_dict()

    # SALARY DATA
    def salary_data(self):
        docs = db.collection(u'alian_software').document(u'employee').collection('employee').document(
            str(self.id)).collection('salaryslips').stream()
        data_dict = {}
        for doc in docs:
            data_dict.update({doc.id: doc.to_dict()})
        print(data_dict)
        return data_dict


