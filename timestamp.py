import time
from datetime import datetime

class TimeStamp:
    def __init__(self):
        self.timeStamp = datetime.now()

        
        tempTime = str(datetime.now().strftime("%H:%M:%S")).split(":")
        self.time = (int(tempTime[0]), int(tempTime[1]), int(tempTime[2]))

        tempDate = str(datetime.now())[0:11].split("-")
        self.date = (int(tempDate[0]), int(tempDate[1]), int(tempDate[2]))

    def getTime(self):
        return self.time
    
    def getDate(self):
        return self.date
    
    def dateToString(self):
        return str(self.date[1]) + "/" + str(self.date[2]) + "/" + str(self.date[0])
    
    def timestampToString(self):
        return dateToString + "\t" + str(self.time[0]) + ":" + str(self.time[1]) + ":" + str(self.time)