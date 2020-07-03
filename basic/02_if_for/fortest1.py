str1 = "abcdefg"
list1 = [1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5)
dic1 = {1: "첫 번째", 2: "두 번째"}
set1 = {1, 2, 3, 4, }

for i in range(2, 10):
    i = int(i)
    for j in range(2, 10):
        j = int(j)
        print("{} * {} = {}".format(i, j, i*j))
    print("-"*10)

for i in range(1, 10):
    i = int(i)
    for j in range(2, 10):
        j = int(j)
        print("{} * {} = {:>2}".format(j, i, j*i), end=" | ")
    print("")

a = [1, 2, 3, 4, 5, ]
result = [i*3 for i in a if i % 2 == 0]

print(result)
