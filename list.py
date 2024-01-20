#list

myList1 = [True, 13, "Hello", [False, "world"]]
#由0開始

print(myList1[3][1])

myList = [0,1,2,3,4,5,6]
print(myList[0:7:2])
#[開始, 終止 (不計算在內), 步數]
#負數代表倒數

print(myList[-2])

count = 0
for i in myList1:
    print(count, i)
    count = count + 1

#enumerate 可以紀錄 index 和 data
for count, i in enumerate(myList1):
    print(count, i)

for i in range(len(myList1)):
    print(myList1[i])

myList = [0,1,2,3,4,5,6]
print(myList)
myList.append(7)
print(myList)

x = myList.pop()
print(myList)
print(x)

myList.extend([7,8,9])
print(myList)


myList = [100,200,300,400,500]
#[500,400,300,200,100]
