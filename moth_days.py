import holidays
import datetime
import calendar



class Month_count():
    def count(self,holidays):
        # Get current year and month
        today = datetime.date.today()
        year = today.year
        month = today.month
        # Get number of days in the current month and the day of the week of the first day
        first_day, num_days  = calendar.monthrange(year, month)
        # Loop through days and count working days
        num_working_days = 0
        Week_off = 0
        working_days_per_week = {}
        # holidays=holidays.keys()
        holiday=0

        # print(first_day)
        # Get the number of days in the current month
        num_days = calendar.monthrange(year, month)[1]

        # Create a list of all the dates in the current month
        dates = [f"{year:04}-{month:02}-{day:02}" for day in range(1, num_days+1)]

        # Print the list of dates
        # print(dates)

        # print(holidays.keys())
        data={}
        if holidays!=None:
            for day in range(1, num_days + 1):
                # print(dates[day - 1])

                if dates[day-1] in holidays :
                    holiday += 1
                elif calendar.weekday(year, month, day) not in (calendar.SATURDAY, calendar.SUNDAY):
                    num_working_days += 1
                else:
                    Week_off += 1


            data = {
                'weekoff': Week_off,
                'workingDays': num_working_days,
                'holydays': holiday
            }
        return data

    def get_holidays(self,holidays):
        # Convert the date strings to datetime objects

        # data = {'2023-04-29': 'xxxxxxxxxx', '2023-04-28': 'xxxxxxxxxx', '2023-01-14': 'xxxxxxxxx',
        #         '2023-04-26': "{'date': '', 'description': ''}"}

        # Convert the date strings to datetime objects
        # Convert the date strings to datetime objects
        sorted_data = {}
        if holidays != None:
            date_objs = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in holidays.keys()]
            # Group the data by month
            data_by_month = {}
            for date_obj, value in zip(date_objs, holidays.values()):
                month_str = date_obj.strftime('%B %Y')
                if month_str not in data_by_month:
                    data_by_month[month_str] = {}
                data_by_month[month_str][date_obj] = value

            # Sort the data by month and date

            for month_str in sorted(data_by_month.keys(), key=lambda x: datetime.datetime.strptime(x, '%B %Y')):
                sorted_data[month_str] = {}
                for date_obj in sorted(data_by_month[month_str].keys()):
                    date_str = date_obj.strftime('%Y-%m-%d')
                    value = data_by_month[month_str][date_obj]
                    sorted_data[month_str][date_str] = value
        return sorted_data
