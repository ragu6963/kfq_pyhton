# 2020 07 08
# 클래스 기본 수업 2


class Person:
    count = 0

    def __init__(self, name, age=1):
        self.name = name
        self.__age = age
        Person.count += 1
        print("{} ({}) is init ".format(name, age))

    def work(self, company):
        print("{}is working in ".format(company))
        self.__getage()

    def sleep(self):
        print("{} is sleeping".format(self.getname()))

    def __getage(self):
        return self.__age

    def getname(self):
        return self.name

    @classmethod
    def getcount(cls):
        return cls.count


obj1 = Person("hong")
obj2 = Person("JEONG",27)

obj1.work("ABC")
obj2.sleep()

print(obj1.getname())
print(obj1._Person__age)
print(obj2._Person__age)

print(Person.getcount())
Person                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      .count = 8
print(Person.getcount())

