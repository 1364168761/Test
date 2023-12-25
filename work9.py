import random
import time

import matplotlib.pyplot as plt
import math

#蛮力
def Brute(arr):
    n = len(arr)
    temp = arr.copy()
    ans = []
    for i in range(n-1):
        for j in range(i+1,n):
            dis = math.sqrt((temp[i][0] - temp[j][0]) ** 2 + (temp[i][1] - temp[j][1]) ** 2)
            ans.append([temp[i], temp[j], dis]) #点1，点2，距离
    ans = sorted(ans,key=lambda point : point[2]) #根据距离排序
    endans = [ans[0][0],ans[0][1]]
    return endans

#分治
    #①按x排序
    #②按x中位数分两部分
    #③重复①②，直到点数<=3              //防止处理点数为1的情况
    #④计算每个小集合的最近邻接点对，及其距离
    #⑤合并最近的两个小集合，按x中位数划分，集合的最近邻接点取较小值    //检查跨越边界的点对
    #⑥保留到中位线距离小于点对距离的点  //筛选
    #⑦若中位线左边和右边均不为空，计算跨界的最近邻接点对，并与已有最近邻接点对比较取较小值
    #⑧重复⑤⑥⑦，直到集合只有一个
    #⑨返回当前集合的最近邻接点对
def distance(p1, p2):   #求距离
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_closest_pair(points):  #分治方法
    if len(points) <= 3:
        #求点集合中点对距离最小的，返回(点1，点2，距离)
        return min(((points[i], points[j], distance(points[i], points[j])) for i in range(len(points)) for j in range(i+1, len(points))), key=lambda x: x[2])

    points.sort(key=lambda x: x[0]) #按x排序
    #分两半
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]

    #继续递归调用，直到满足返回条件 <=3
    closest_left = find_closest_pair(left_half)
    closest_right = find_closest_pair(right_half)

    #取左右两半最小点对的较小者
    closest_pair = closest_left if closest_left[2] < closest_right[2] else closest_right

    mid_x = points[mid][0] #取中间数的x
    strip = [point for point in points if abs(point[0] - mid_x) < closest_pair[2]] #abs()取绝对值，这里保留到中位线距离小于点对距离的点

    strip.sort(key=lambda x: x[1]) #根据y排序

    return merge_closest_pair(strip, closest_pair) #经过跨界点对处理

def merge_closest_pair(strip, closest_pair): #跨界点对处理
    min_dist = closest_pair[2] #最近邻接点对的距离
    closest_points = closest_pair #temp

    #
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:   #比较y和已求距离的大小
                break
            d = distance(strip[i], strip[j])
            #更新最小距离，点对
            if d < min_dist:
                min_dist = d
                closest_points = strip[i], strip[j], d

    return closest_points

# 示例用法
x,y = [],[]
arr = []
for i in range(10): #修改n
    x.append(random.randint(1,200))
    y.append(random.randint(1,200))
for i in range(10): #修改n
    arr.append((x[i],y[i]))

#初始化
x,y = [],[]
arr = []
n = [] #规模,x轴
t1,t2 = [],[] #执行时间，y轴
for i in range(10,500):
    n.append(i)
    for j in range(i):
        x.append(random.randint(1,200))
        y.append(random.randint(1,200))
    for m in range(i):
        arr.append((x[m],y[m]))

    print('蛮力：')
    T1 = time.perf_counter()
    print(Brute(arr))
    T2 = time.perf_counter()
    t1.append(T2-T1)
    print('分治')
    T1 = time.perf_counter()
    print(find_closest_pair(arr))
    T2 = time.perf_counter()
    t2.append(T2-T1)
    #重置
    x, y = [], []
    arr = []


#展示
plt.figure(figsize=(10, 10))
plt.subplot(221)
plt.scatter(n, t1)
plt.title('Brute')
plt.subplot(222)
plt.scatter(n,t2)
plt.title('Divide')
plt.show()
