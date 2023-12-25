import copy
import time


# 单元格类型
# 0 - 路，1 - 墙，2-走过的路，3-死胡同
class CellType:
    ROAD = 0
    WALL = 1
    WALKED = 2
    DEAD = 3


# 墙的方向
class Direction:
    LEFT = 0,
    UP = 1,
    RIGHT = 2,
    DOWN = 3,


def valid(maze, x, y):
    if x < 0 or y < 0:
        return False
    if x >= len(maze) or y >= len(maze):
        return False
    val = maze[y][x]
    if val == CellType.WALL or val == CellType.DEAD: #墙或死胡同
        return False
    return val, x, y


def neighbors(maze, pos):
    x, y = pos
    #val,x,y     ;左，上，右，下
    t, r, d, l = valid(maze, x, y - 1), valid(maze, x + 1, y), valid(maze, x, y + 1), valid(maze, x - 1, y)
    return t, r, d, l


def mark_walked(maze, pos):
    maze[pos[1]][pos[0]] = CellType.WALKED #走过了


def mark_dead(maze, pos):
    maze[pos[1]][pos[0]] = CellType.DEAD


def suggest_pos(cells): #传入点集
    arr = []
    for cell in cells:
        if cell:
            arr.append(cell[0]) #(t,r,d,l)
        else:
            arr.append(CellType.DEAD)
    return cells[arr.index(min(arr))] #返回能走的上、下、左、右中val值最小的，因为其中0,1,2,3分别代表路，墙，走过，死胡同


def solve_maze(maze, pos, end, callback): #pos:start,end:exit，callback:draw_maze(maze,cur_pos)函数
    time.sleep(0.05) #延迟
    # 到达出口
    if pos[0] == end[0] and pos[1] == end[1]: #x,y相等
        mark_walked(maze, pos)
        return True #找到出口
    # 获取相邻4个位置
    t, r, d, l = neighbors(maze, pos) #左，上，右，下
    next_pos = suggest_pos((t, r, d, l)) #确定下一步方向
    if next_pos: #如果有下一步
        if next_pos[0] == CellType.WALKED: #val == 2，走过
            mark_dead(maze, pos) #走，并使该点val = 3
        else: #val == 0， 路
            mark_walked(maze, pos) #走，并使该点val = 2
        callback(maze, next_pos) #使用draw_maze函数绘制迷宫，pygame实现
        return solve_maze(maze, (next_pos[1], next_pos[2]), end, callback) #更新当前点递归调用
    else: #如果没有下一步
        mark_dead(maze, pos)#则标记当前点为死胡同
        callback(maze, next_pos)
        return False#返回找不到出口

def dfs_maze(maze, start, end, visited):
    maze1 = copy.copy(maze)
    start1 = tuple([start[1], start[0]])
    end1 = tuple([end[1], end[0]])

    if start1 == end1:
        return True  # 找到了终点

    visited.add(start1)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(maze1), len(maze1[0])

    for direction in directions:
        new_row, new_col = start1[0] + direction[0], start1[1] + direction[1]
        if 0 <= new_row < rows and 0 <= new_col < cols and maze1[new_row][new_col] == 0 and (new_row, new_col) not in visited:
            if dfs_maze(maze1, (new_row, new_col), end1, visited):
                return True,visited

    return False  # 无法到达终点

from collections import deque

def bfs_maze(maze, start, end):
    maze1 = copy.copy(maze)
    start1 = tuple([start[1], start[0]])
    end1 = tuple([end[1], end[0]])

    queue = deque([start1])
    visited = set()
    visited.add(start1)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(maze1), len(maze1[0])

    while queue:
        current = queue.popleft()
        if current == end1:
            return True,visited  # 找到了终点

        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and maze1[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

    return False  # 无法到达终点