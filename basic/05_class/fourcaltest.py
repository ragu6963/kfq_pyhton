class FourCal: 
    def __init__(self,first=1 ,second = 4):
        self.first = first
        self.second=second
        print("생성자")

    def __str__(self):
        return "num1 = %d, num2 = %d"%(self.first,self.second)

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def div(self):
        return self.first / self.second

class MoreFourlCal(FourCal):
    def pow(self):
        return self.first ** self.second

    def div(self):
        if self.second != 0:
            return self.first / self.second
        else:
            return 0 

cal1 = MoreFourlCal()
cal2 = MoreFourlCal(2,0)
print(cal1.add())
print(cal2.add())
print(cal2.div())

