import datetime
import time

print(datetime.datetime.now())

filename = datetime.datetime.now()#Assigns filename current time

with open (filename.strftime("%Y-%m-%d-%H-%M")+".txt", 'w') as file:#Opens new file of name format Year-Month-Day-Hour-Minutes.txt
    
    file.write(str(datetime.datetime.now()))#Writes string of current time to file

timeList = []

for i in range(5):

    timeList.append(datetime.datetime.now())
    time.sleep(1)#delays for 1 sec

with open("timelog.txt",'r+') as file:

    file.read()

    for time in timeList:

        file.write(str(time)+'\n')

    start = timeList[0]
    end = timeList[-1]

    diff = end - start

    file.write(str(diff)+'\n')
