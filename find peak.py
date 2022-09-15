def findPeak(arr, n) :
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
    for i in range(1, n - 1) :
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
arr = []
ah=int(input("enter the limit for the list"))
for i in range(0,ah):
    ha=int(input())
    arr.append(ha)
print(arr)
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))


output:
  enter the limit for the list4
1
2
3
1
[1, 2, 3, 1]
Index of a peak point is 2
