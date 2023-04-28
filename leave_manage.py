import datetime
import concurrent.futures

class Leavemanage():
    def __init__(self, db):
        self.db = db

    def leave_add(self, companyname):
        if datetime.date.today().day == 13:
            users_ref = self.db.collection(companyname).document('employee').collection('employee').document(
                'empid').collection('leaveMST')
            leaves = users_ref.document('total_leaves').get().to_dict()
            users_ref.document('total_leaves').set({
                'SL': (leaves['SL'] + 0.5),
                'PL': (leaves['PL'] + 1),
                'CL': (leaves['CL'] + 0.5)
            })

    def take_leave(self, ref_obj, data=None):
        if data == None:
            print('Error')
        else:
            data_dict = {}
            leaves = ref_obj.document('total_leaves').get().to_dict()
            for key, value in data.items():
                data_dict.update({key: value})
            if int(leaves[data_dict['type']]) - int(data_dict['days']) > 0:
                ref_obj.document('total_leaves').update({
                    data_dict['type']: (leaves[data_dict['type']] - int(data_dict['days']))
                })
            else:
                ref_obj.document('total_leaves').update({
                    'LWP': (leaves['LWP'] + int(data_dict['days']))
                })
            data = ref_obj.document(data_dict['applydate']).set(data_dict)

    def take_leave_edit(self, ref_obj, data=None):
        if data == None:
            print('Error')
        else:
            data_dict = data
            leaves = ref_obj.document('total_leaves').get().to_dict()
            if int(leaves[data_dict['type']]) - int(data_dict['days']) > 0:
                ref_obj.document('total_leaves').update({
                    data_dict['type']: (leaves[data_dict['type']] - int(data_dict['days']))
                })
            else:
                ref_obj.document('total_leaves').update({
                    'LWP': (leaves['LWP'] + int(data_dict['days']))
                })
            data = ref_obj.document(data_dict['applydate']).set(data_dict)

    def get_total_leave(self, ref_obj):
        data = ref_obj.document('total_leaves').get().to_dict()
        return data

    def leave_list(self, ref_obj):
        docs = ref_obj.stream()
        data_dict = {}
        for doc in docs:
            data_dict.update({doc.id: doc.to_dict()})
        return data_dict

    def process_leave_add(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.leave_add)

    def process_take_leave(self, ref_obj, data=None):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.take_leave, ref_obj, data)

    def process_take_leave_edit(self, ref_obj, data=None):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.take_leave_edit, ref_obj, data)

    def process_get_total_leave(self, ref_obj):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_total_leave, ref_obj)
            return future.result()

    def process_leave_list(self, ref_obj):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.leave_list, ref_obj)
            return future.result()
