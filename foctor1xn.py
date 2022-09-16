num=int(input("enter the number"))
nfactor=int(input("enter n value"))
total=0
count=0
factors=[]
for i in range(1,num+1):
    if(num%i==0):
        total=total+1
        if(count<nfactor):
            factors.append(i)
            count=count+1
            print("total factor is ",total)
            if(nfactor>total):
                print("it has only",total,"factors")
else:
     print("n factors are",factors)
    
    output:
      enter the number100
enter n value4
total factor is  1
it has only 1 factors
total factor is  2
it has only 2 factors
total factor is  3
it has only 3 factors
total factor is  4
n factors are [1, 2, 4, 5]
