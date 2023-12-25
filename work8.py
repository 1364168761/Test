import random
import time


def binarySearch(arr,start,end,x):
   if end >= start:
      mid = int( start+(end-start)/2 )
      if arr[mid] == x:
         return mid
      if arr[mid] > x:
         return binarySearch(arr,start,mid-1,x)
      return binarySearch(arr,mid+1,end,x)
   return -1
def ternarySearch(arr,start,end,x):
   if end >= start:
      mid1 = int(start + (end-start)/3)
      mid2 = int(mid1+(end-start)/3)
      if arr[mid1] == x:
         return mid1
      if arr[mid2] == x:
         return mid2
      if arr[mid1] > x:
         return ternarySearch(arr,start,mid1-1,x)
      if arr[mid2] < x:
         return ternarySearch(arr,mid2+1,end,x)
      return ternarySearch(arr,mid1+1,mid2-1,x)
   return -1

#test
arr = []
for i in range(10000):
    arr.append(random.randint(1,20000))
x = arr[44]
arr.sort()

for i in range(1,4):
   print(f'第{i}次')
   print('二分')
   start = 1
   end = len(arr) - 1
   T1 = time.perf_counter()
   binarySearch(arr,start,end,x)
   T2 = time.perf_counter()
   print(f'程序运行时间:{T2 - T1}微秒')

   print('------------------')

   print('三分')
   start = 1
   end = len(arr) - 1
   T1 = time.perf_counter()
   ternarySearch(arr,start,end,x)
   T2 = time.perf_counter()
   print(f'程序运行时间:{T2 - T1}微秒')

