myList=[]
e=int(input("enter the limit for the list"))
for i in range(0,e):
    z=int(input())
    myList.append(z)
print(myList)
dupItems = []
uniqItems = {}
print("List = ",myList)

for x in myList:
	if x not in uniqItems:
		uniqItems[x] = 1
	else:
		if uniqItems[x] == 1:
			dupItems.append(x)
		uniqItems[x] += 1
print("Duplicate Elements = ",dupItems)


output:
  enter the limit for the list5
15
25
31
32
15
[15, 25, 31, 32, 15]
List =  [15, 25, 31, 32, 15]
Duplicate Elements =  [15]
