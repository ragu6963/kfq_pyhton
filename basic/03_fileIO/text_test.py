f = open("text.txt",'w',encoding="UTF-8")
f.write("파일 생성\n")
f.write("파일 생성\n")
f.write("파일 생성\n")
f.write("파일 생성\n")
f.write("파일 생성\n")
f.write("파일 생성\n") 

f.close()

f = open("text.txt",'r',encoding="UTF-8")
lines = f.readlines()
for i in lines:
    print(i,end="")

f.close()