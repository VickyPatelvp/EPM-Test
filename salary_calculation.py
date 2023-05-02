import datetime
from tds_data import TDSData


class SalaryCalculation():

    def __init__(self,db):
        self.db = db

    def generate_salary(self, companyname, workingday):

        working_days = workingday

        # current_month = datetime.datetime.now().month

        current_month = 5

        if current_month == 1:
            month = 13 - current_month
        else:
            month = current_month - 1

        year = datetime.datetime.now().year
        if current_month == 1:
            year = year - 1
        else:
            year=year

        salary_percentage = (self.db.collection(companyname).document('salary_calc').get()).to_dict()

        employee_list = {}

        employee_data = (self.db.collection(companyname).document('employee').collection('employee').stream())

        for doc in employee_data:
            employee_list.update({doc.id: doc.to_dict()})

        for key,value in employee_list.items():

            empid = key

            emp_data = value

            emp_name = emp_data['employeeName']

            emp_salary = emp_data['salary']

            # emp_salary = 50000

            lwp = 0

            emp_basic_salary = round(float(emp_salary) * float(float(salary_percentage['hrapercentage'])/100), 2)

            emp_hra = round(emp_basic_salary * float(float(salary_percentage['hrapercentage'])/100), 2)

            emp_da = round(emp_basic_salary * float(float(salary_percentage['dapercentage'])/100), 2)

            other_allowance = 0

            incentive = 0

            arrears = 0

            grs_outstanding_adjustment = 0

            statutory_bns = 0

            gross_salary = round((emp_basic_salary + emp_hra + emp_da + other_allowance + incentive + arrears +
                                  grs_outstanding_adjustment + statutory_bns), 2)

            epfo = round((emp_basic_salary * 3.2 / 100), 2)

            if epfo <= 1800:
                epfo=epfo
            else:
                epfo=1800

            ded_outstanding_adjustment = 0

            pt = 200

            tds = TDSData(db=self.db).deduction(empid,companyname)

            other_deduction = 0

            if lwp > 0:
                leave_deduction = lwp * (round((float(emp_salary)/working_days * float(salary_percentage['deductionpercentage'])), 2))
            else:
                leave_deduction = 0

            total_deduction = round((epfo + ded_outstanding_adjustment + pt + tds + other_deduction + leave_deduction), 2)

            net_salary = round((gross_salary - total_deduction), 2)

            salary_slip_data = {
                'employeeName': emp_name, 'userID': empid,'slip_id': f'sal00{current_month-1}', 'lwp': lwp,
                'basic': emp_basic_salary, 'da': emp_da, 'hra': emp_hra, 'otherAllowance': other_allowance,
                'incentive': incentive, 'grsOutstandingAdjustment': grs_outstanding_adjustment, 'arrears': 0,
                'statutoryBonus': statutory_bns, 'grossSalary': gross_salary, 'epfo': epfo,
                'dedOutstandingAdjustment': ded_outstanding_adjustment, 'pt': pt, 'tds': tds,
                'otherDeduction': other_deduction, 'leaveDeduction': leave_deduction, 'totalDeduction': total_deduction,
                'netSalary': net_salary, 'month': month, 'year': year
                            }

            users_ref = self.db.collection(u'alian_software').document('employee').collection('employee').document(empid)

            if current_month == 1:
                users_ref.collection('salaryslips').document(f'sal00{month}').set(salary_slip_data)
            else:
                users_ref.collection('salaryslips').document(f'sal00{month}').set(salary_slip_data)

            # print(salary_slip_data)












