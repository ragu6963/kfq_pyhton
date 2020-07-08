#  2020 07 07
#  클래스 기본 수업

class FourCal:
    mode = 1
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

a = FourCal()
# a.setdata(3,6)
a.mode = 1

print(a.first)
print(a.second)
print(a)
print(a.add())