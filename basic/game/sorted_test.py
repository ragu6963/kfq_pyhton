mylist=[4,2,3,5,1]
mylist.sort()
print(mylist)
myDic = {1:1,3:3,2:5}

sorted(myDic.items(),reverse=True,key=lambda x:x[1])

sorted(["abc",'bac','python'],key=lambda x:x[1],reverse=True)


