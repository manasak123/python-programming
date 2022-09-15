salary=int((input("enter the salary")))
if(salary<=0):
    print("invalid")
else:
    grade=input("enter the grade")
    if(grade=='A' or grade=='a'):
        if(salary<10,000):
            bonus=0.07
            h=salary*bonus
            print("bonus:",h)
            total=salary+h
            print("the total salary is :",total)
        elif(salary>=10000):
            bonus=0.05
            h=salary*bonus
            print("bonus:",h)
            total=salary+h
            print("the total salary is:",total)
    if(grade=='B' or grade=='b'):
       if(salary<10000):
            bonus=0.12
            h=salary*bonus
            print("bonus",h)
            total=salary+h
            print("the total salary is:",total)
        elif(salary>=10000):
            bonus=0.1
            h=salary*bonus
            print("bonus:",h)
            total=salary+h
            print("the total salary is:",total)
    else:
        print("invalid")

        
        output:
          enter the salary50000
enter the gradeb
bonus: 5000.0
the total salary is: 55000.0
