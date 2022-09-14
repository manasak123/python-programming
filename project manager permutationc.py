import itertools
st=input("enter the number")
per=itertools.permutations(st)
for val in per:
    print(*val)
