from datetime import datetime

# Sample datetime object
dt2 = datetime.today().date()
dt2_str = '2022-03-01'
dt1 = datetime.strptime(dt2_str, '%Y-%m-%d')
diff = (dt2.year - dt1.year) * 12 + (dt2.month - dt1.month)
# Output: 14
class Dashboard():
    def __init__(self,db):
        self.db=db
    def employee_on_lerave(self):
        users_ref = self.db.collection(u'alian_software').document('employee').collection('employee')
        total_leaves={}
        for emp_doc in users_ref.stream():
            leaves=users_ref.document(emp_doc.id).collection('leaveMST')
            for leave in leaves.stream():
                if leave.id != 'total_leaves' and leave.id != 'date' :
                    dt2 = datetime.today().date()
                    dt1 = datetime.strptime(leave.id, '%Y-%m-%d')
                    diff = (dt2.year - dt1.year) * 12 + (dt2.month - dt1.month)
                    if diff<2:
                        total_leaves.update({users_ref.document(emp_doc.id).get().to_dict()['employeeName']:leaves.document(leave.id).get().to_dict()['fromdate']})
           
        return total_leaves

    def total_lerave(self):
        users_ref = self.db.collection(u'alian_software').document('employee').collection('employee')
        total_leaves = {}
        for emp_doc in users_ref.stream():
            leaves = users_ref.document(emp_doc.id).collection('leaveMST')
            name=users_ref.document(emp_doc.id).get().to_dict()['employeeName']
            total_leaves.update({name:0})
            for leave in leaves.stream():
                if leave.id != 'total_leaves':
                    total_leaves.update({name: total_leaves[name]+ int(leaves.document(leave.id).get().to_dict()['days'])})
             
        return total_leaves

