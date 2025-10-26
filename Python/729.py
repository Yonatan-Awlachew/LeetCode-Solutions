class MyCalendar:

    def __init__(self):
        self.store=[]

    def book(self, startTime: int, endTime: int) -> bool:
        for i,j in self.store:
            if startTime<j and endTime>i:
                return False
        self.store.append((startTime,endTime))
        return True
