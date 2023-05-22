import datetime


st=datetime.datetime.now()
squared_numbers = []


for num in range(0,1000):
    squared_numbers.append(num**2)

endt=datetime.datetime.now()



st=datetime.datetime.now()
squared_numbers = [num**2 for num in range(0,1000)]

endt=datetime.datetime.now()
