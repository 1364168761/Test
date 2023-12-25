import networkx as nx
import matplotlib.pyplot as plt

# 定义一个图
G = nx.Graph()
# 添加边和权重
G.add_edge(0, 1, weight=4)
G.add_edge(1, 2, weight=8)
G.add_edge(2, 5, weight=2)
G.add_edge(1, 3, weight=7)
G.add_edge(2, 4, weight=9)
G.add_edge(3, 4, weight=10)

# 使用Kruskal算法生成最小生成树
#初始化每个结点的父节点为自身
f = []
for i in range(len(G.nodes)):
    f.append(i)

#初始化每条边 u，v,w-》左点，右点，权重
edges = []
for u, v, w in G.edges(data=True):
    edges.append([u,v,w['weight']])

#所有边排序，权重低到高
edges = sorted(edges,key=lambda edge: edge[2])

#findroot
def find(x):
    global f
    if (x == f[x]): #找到根结点
        return x
    else:
        f[x] = find(f[x])#路径压缩，即将x的根结点f[x]设为直到满足x==f[x]的结点
        return  f[x]

#构造最小生成树
G1 = nx.Graph()
count = 0
for edge in edges:
    if count >= len(f) - 1: #最小生成树的边有n-1个，n为结点个数
        break
    u = find(edge[0])
    v = find(edge[1])
    if (u==v): #根结点相同，此时在两边均与根结点相连的情况下，连接任意第三边会构成环路，故跳过
        continue
    G1.add_edge(u,v , weight=edge[2])
    count += 1

#展示
pos = nx.spring_layout(G1)  # 定义节点位置
edge_labels = {(u, v): d['weight'] for u, v, d in G1.edges(data=True)}  # 提取边的权重作为标签
nx.draw(G1, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold', edge_color='gray', width=2)
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels)  # 添加边的权重标签
plt.show()

