import datetime

class Leavemanage():
    def __init__(self,db):
        self.db=db
    def leave_add(self):
        if datetime.date.today().day==13:
            users_ref = self.db.collection(u'alian_software').document('employee').collection('employee').document(
                'empid').collection('leaveMST')
            leaves=users_ref.document('total_leaves').get().to_dict()
            print(leaves)
            users_ref.document('total_leaves').set({
                'SL': (leaves['SL']+0.5),
                'PL': (leaves['PL']+1),
                'CL': (leaves['CL']+0.5)
            })

    def take_leave(self,ref_obj,data=None):
        # doc_ref = users_ref.document(str(datetime.date.today().month))
        # doc_ref.set(data)
        if data==None:
            print('Error')
        else:
            data_dict={}
            leaves=ref_obj.document('total_leaves').get().to_dict()
            print(leaves)
            for key,value in data.items():
                data_dict.update({key:value})
            print(data_dict)

            if leaves[data_dict['type']] - int(data_dict['days'])>0:
                ref_obj.document('total_leaves').update({
                    data_dict['type']: (leaves[data_dict['type']] - int(data_dict['days']))
                })
            else:
                ref_obj.document('total_leaves').update({
                    'LWP': (leaves['LWP'] + int(data_dict['days']))
                })
            print(data_dict)
            data = ref_obj.document(data_dict['applydate']).set(data_dict)


        pass


    def get_total_leave(self,ref_obj):
        data=ref_obj.document('total_leaves').get().to_dict()
        return data

    def leave_list(self,ref_obj):
        docs = ref_obj.stream()
        data_dict={}
        for doc in docs:
            # print(f'{doc.id} => {doc.to_dict()}')
            data_dict.update({doc.id:doc.to_dict()})
        return  data_dict

    def show(self):
        print(self.db)


