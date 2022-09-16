def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num =int(input("enter the number"))

print_factors(num)

output:
enter the number100
The factors of 100 are:
1
2
4
5
10
20
25
50
100
