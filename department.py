import re
from firebase_admin import credentials
from firebase_admin import firestore
import concurrent.futures

# cred = credentials.Certificate('empoyee-payroll-system-firebase-adminsdk-5h89d-bc19d4a8c9.json')
#
# db = firestore.client()


class Department:
    def __init__(self, db):
        self.db = db

    def _process_department(self, data):
        doc_ref = self.db.collection(u'alian_software').document(u'department')
        is_available = False
        for key, value in doc_ref.get().to_dict().items():
            if key == data['deptname'] and value != {}:
                is_available = True
        if is_available == True and len(data.items()) == 1:
            doc_ref.update({f'{data["deptname"]}.{data["pos0"]}': data['sal0']})
        else:
            pos = []
            sal = []
            deptnm = ''
            for key, value in data.items():
                if key == 'deptname':
                    deptnm = value
                elif re.findall("^pos", key):
                    pos.append(value)
                elif re.findall("^sal", key):
                    sal.append(value)


            data = {p: s for p, s in zip(pos, sal)}

            doc_ref.update({deptnm: data})

    def add_department(self, result):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self._process_department, result)

    def delete_department(self, dept, pos):
        doc_ref = self.db.collection(u'alian_software').document(u'department')
        position = dept + '.' + pos
        doc_ref.update({position: firestore.DELETE_FIELD})
        if doc_ref.get().to_dict()[dept] == {}:
            doc_ref.update({dept: firestore.DELETE_FIELD})
