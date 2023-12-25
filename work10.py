import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


# 生成随机有向图
def generate_random_digraph (n, edge_probability):
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < edge_probability:
                G.add_edge(i, j)
    return G


# 检查图中是否存在环
def has_cycle (G):
    return any(nx.simple_cycles(G)) #nx.simple_cycles(G)返回多个判断结果，用any判断，若有True则返回True


#绘柱状图图
def bar_picture(categories,has,notHas):
    # 设置柱状图的宽度
    bar_width = 0.35

    # 计算每组柱状图的中心位置
    r1 = np.arange(len(categories))
    r2 = [x + bar_width for x in r1]

    # 画图
    plt.bar(r1, has, color='b', width=bar_width, edgecolor='grey', label='has')
    plt.bar(r2, notHas, color='r', width=bar_width, edgecolor='grey', label='notHas')

    # 添加标签
    plt.xlabel('variable', fontweight='bold')  # 变量
    plt.ylabel('number', fontweight='bold')  # 次数
    plt.xticks([r + bar_width / 2 for r in range(len(categories))], categories)

    # 添加图例
    plt.legend()  # 不同演示柱子说明

    # 显示图形
    plt.show()



# 参数, n:顶点个数，edge_probability:概率
# n = {5~20},pro=0.3  -> pro 保持不变,每个n测3次
categories = [] #标记变量
has = [] #有环次数
notHas = [] #无环次数
edge_probability = 0.3

for n in range(5, 21):
    categories.append(n)
    has.append(0)
    notHas.append(0)
    for i in range(3):
        random_digraph = generate_random_digraph(n, edge_probability)
        if has_cycle(random_digraph):
            has[n-5] += 1
        else:
            notHas[n-5] += 1
bar_picture(categories, has, notHas)

# n = 5,pro={0.3~1} -> n保持不变，每个pro测3次
categories = [] #标记变量
has = [] #有环次数
notHas = [] #无环次数
n = 5
count = 0 #has,notHas的索引
for edge_probability in np.arange(0.3, 1.1, 0.1):
    edge_probability = round(edge_probability, 2) #保留两位小数
    categories.append(edge_probability)
    has.append(0)
    notHas.append(0)
    for i in range(3):
        random_digraph = generate_random_digraph(n, edge_probability)
        if has_cycle(random_digraph):
            has[count] += 1
        else:
            notHas[count] += 1
    count += 1
bar_picture(categories, has, notHas)



