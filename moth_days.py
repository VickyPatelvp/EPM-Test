import holidays
import datetime
import calendar



class Month_count():
    def count(self):
        # Get current year and month
        today = datetime.date.today()
        year = today.year
        month = today.month
        # Get number of days in the current month and the day of the week of the first day
        num_days, first_day = calendar.monthrange(year, month)
        # Loop through days and count working days
        num_working_days = 0
        Week_off =0
        working_days_per_week = {}
        for day in range(1, first_day+1):
            if calendar.weekday(year, month, day) not in (calendar.SATURDAY, calendar.SUNDAY):
                num_working_days += 1
            else:
                Week_off +=1

        # Create instance of holidays class for the US
        us_holidays = holidays.US()

        # Get dictionary of holidays for current month and year
        month_holidays = us_holidays[
                         datetime.date(year, month, 1):datetime.date(year, month, calendar.monthrange(year, month)[1])]
        holiday=len(month_holidays)
        num_working_days=num_working_days-holiday
        data={
            'weekoff':Week_off,
            'workingDays': num_working_days,
            'holydays': holiday
        }
        return data

#     comp->employee->employe->eomployeeid->leave->docu(lwave)->adf *100
# leave->docu(lwave)->ad *100