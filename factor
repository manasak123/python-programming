num = int(input("Enter a number :"))
count = 0
print("The factors of",num,"are",end=" ")
for i in range(1, num+1, 1):
    if(num % i == 0):
        count = count + 1
        print(i, end = " ")
print("\nTotal factors of",num,":",count)
