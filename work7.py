import heapq


def dijkstra (graph, start):
    # 初始化距离字典，用于记录每个节点到起点的距离
    #float('inf')表示正无穷
    dist = {node: float('inf') for node in graph}
    dist[start] = 0 #源点到自身距离为0

    # 初始化堆
    heap = []
    heapq.heappush(heap, (0, start))

    # 循环堆
    while heap:
        (distance, current_node) = heapq.heappop(heap) #（0，start）

        # 当前节点已经求出最短路径
        if distance > dist[current_node]:
            continue

        # 遍历当前节点的相邻节点
        for neighbor, weight in graph[current_node].items():
            dist_neighbor = dist[current_node] + weight #源点到current_node的距离+current_node到dist_neighbor的距离
            # 更新最短路径距离
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                heapq.heappush(heap, (dist_neighbor, neighbor))
    t = 3
    results = list(filter(lambda i: i <= t, dist.values()))
    flag = False
    if len(results) == len(dist.values()):
        flag = True
    return flag


# 测试代码
graph = {'湖北省': {'河南省': 1, '安徽省': 1,'江西省':1,'湖南省':1,'重庆市':1,'陕西省':1},
         '北京市': {'河北省':1,'天津市':1},
        '天津市': {'北京市':1,'河北省':1},
        '上海市': {'浙江省':1,'江苏省':1},
        '重庆市': {'四川省':1,'贵州省':1,'陕西省':1,'湖北省':1,'湖南省':1},
        '河北省': {'山东省':1,'河南省':1,'山西省':1,'内蒙古自治区':1,'辽宁省':1,'天津市':1,'北京市':1},
        '山西省': {'内蒙古自治区':1,'陕西省':1,'河南省':1,'河北省':1},
        '辽宁省': {'吉林省':1,'内蒙古自治区':1,'河北省':1},
        '吉林省': {'内蒙古自治区':1,'辽宁省':1,'黑龙江省':1},
        '黑龙江省': {'吉林省':1,'内蒙古自治区':1},
         '江苏省': {'山东省':1,'安徽省':1,'浙江省':1,'上海市':1},
        '浙江省': {'江苏省':1,'安徽省':1,'上海市':1,'江西省':1,'福建省':1},
        '安徽省': {'山东省':1,'江苏省':1,'浙江省':1,'江西省':1,'湖北省':1,'河南省':1,},
        '福建省': {'浙江省':1,'江西省':1,'山东省':1},
        '江西省': {'安徽省':1,'浙江省':1,'福建省':1,'广东省':1,'湖南省':1,'湖北省':1},
        '山东省': {'河北省':1,'河南省':1,'安徽省':1,'江苏省':1},
        '河南省': {'河北省':1,'山东省':1,'江苏省':1,'安徽省':1,'湖北省':1,'陕西省':1,'山西省':1},
        '湖南省': {'湖北省':1,'江西省':1,'广东省':1,'广西壮族自治区':1,'贵州省':1,'重庆市':1},
        '广东省': {'福建省':1,'江西省':1,'湖南省':1,'广西壮族自治区':1,'海南省':1,'香港市':1,'澳门市':1},
        '海南省': {'广东省':1},
        '四川省': {'青海省':1,'甘肃省':1,'陕西省':1,'重庆市':1,'贵州省':1,'云南省':1,'新疆维吾尔自治区':1,'西藏自治区':1,},
        '贵州省': {'四川省':1,'重庆市':1,'湖南省':1,'广西壮族自治区':1,'云南省':1},
        '云南省': {'西藏自治区':1,'四川省':1,'贵州省':1,'广西壮族自治区':1},
        '陕西省': {'内蒙古自治区':1,'河南省':1,'湖北省':1,'重庆市':1,'四川省':1,'甘肃省':1,'宁夏回族自治区':1,'山西省':1,},
        '甘肃省': {'内蒙古自治区':1,'宁夏回族自治区':1,'陕西省':1,'四川省':1,'青海省':1,'新疆维吾尔自治区':1},
        '青海省': {'新疆维吾尔自治区':1,'甘肃省':1,'四川省':1,'西藏自治区':1},
        '内蒙古自治区': {'甘肃省':1,'宁夏回族自治区':1,'陕西省':1,'山西省':1,'河北省':1,'辽宁省':1,'吉林省':1,'黑龙江省':1,},
        '广西壮族自治区': {'云南省':1,'贵州省':1,'湖南省':1,'广东省':1},
        '西藏自治区': {'新疆维吾尔自治区':1,'青海省':1,'四川省':1,'云南省':1},
        '宁夏回族自治区': {'内蒙古自治区':1,'陕西省':1,'甘肃省':1},
        '新疆维吾尔自治区': {'甘肃省':1,'青海省':1,'西藏自治区':1},
        '香港市': {'广东省':1},
        '澳门市': {'广东省':1},
         }
print(dijkstra(graph, '湖北省'))
