list1=[]
list2=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    item=int(input())
    list1.append(item)
m=int(input("enter the number of elements:"))
for i in range(0,m):
    element=int(input())
    list2.append(element)
print("the present list 1 is",list1)
print("the present list 2 is",list2)
list3=sorted(list1+list2)
print("the merged list is",list3)
