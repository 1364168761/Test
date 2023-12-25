# coding=utf-8
from random import randint, choice


# 单元格类型
# 0 - 路，1 - 墙
class CellType:
    ROAD = 0
    WALL = 1


# 墙的方向
class Direction:
    LEFT = 0,  #← ↑ → ↓
    UP = 1,
    RIGHT = 2,
    DOWN = 3,


# 迷宫地图
class Maze:

    def __init__(self, width, height):
        self.width = width #宽
        self.height = height #高
        self.maze = [[0 for x in range(self.width)] for y in range(self.height)] #全部初始化为路

    def reset_maze(self, value): #根据value重新初始化图
        for y in range(self.height):
            for x in range(self.width):
                self.set_maze(x, y, value)

    def set_maze(self, x, y, value): #设置单元是墙还是路
        self.maze[y][x] = CellType.ROAD if value == CellType.ROAD else CellType.WALL
        # self.maze[x][y] = CellType.ROAD if value == CellType.ROAD else CellType.WALL
    def visited(self, x, y): #单元[y][x]不是墙吗 （不是则返回True）
        return self.maze[y][x] != 1
        # return self.maze[x][y] != 1

def check_neighbors(maze, x, y, width, height, checklist): #迷宫，点，size，checklist
    directions = []
    #判断相邻点是否是墙，如果不是墙则二者间可以打通，传入点是[2x+1][2y+1]
    if x > 0: #如果[2*y+1][2*(x-1)+1]是墙
        if not maze.visited(2 * (x - 1) + 1, 2 * y + 1): #[2y+1][2x-1]
            directions.append(Direction.LEFT)
    if y > 0:
        if not maze.visited(2 * x + 1, 2 * (y - 1) + 1): #[2y-1][2x+1]
            directions.append(Direction.UP)
    if x < width - 1:
        if not maze.visited(2 * (x + 1) + 1, 2 * y + 1): #[2y+1][2x+3]
            directions.append(Direction.RIGHT)
    if y < height - 1:
        if not maze.visited(2 * x + 1, 2 * (y + 1) + 1): #[2y+3][2x+1]
            directions.append(Direction.DOWN)
    #如果传入点周围有可以打通的路点，则随机选择一个方向打通，最后返回True
    if len(directions):
        direction = choice(directions)
        #前一个set_maze设置目标位置是路
        #后一个set_maze打通当前点与目标点的墙
        #加入目标点未处理的width,height
        if direction == Direction.LEFT:
            maze.set_maze(2 * (x - 1) + 1, 2 * y + 1, CellType.ROAD)
            maze.set_maze(2 * x, 2 * y + 1, CellType.ROAD)
            checklist.append((x - 1, y))
        elif direction == Direction.UP:
            maze.set_maze(2 * x + 1, 2 * (y - 1) + 1, CellType.ROAD)
            maze.set_maze(2 * x + 1, 2 * y, CellType.ROAD)
            checklist.append((x, y - 1))
        elif direction == Direction.RIGHT:
            maze.set_maze(2 * (x + 1) + 1, 2 * y + 1, CellType.ROAD)
            maze.set_maze(2 * x + 2, 2 * y + 1, CellType.ROAD)
            checklist.append((x + 1, y))
        elif direction == Direction.DOWN:
            maze.set_maze(2 * x + 1, 2 * (y + 1) + 1, CellType.ROAD)
            maze.set_maze(2 * x + 1, 2 * y + 2, CellType.ROAD)
            checklist.append((x, y + 1))
        return True
    return False


def random_prime(map, width, height): #(map,m,m) 点为(2*x+1,2*y+1)
    start_x, start_y = (randint(0, width - 1), randint(0, height - 1)) #迷宫最外围默认是墙，这里是避免取到墙
    map.set_maze(2 * start_x + 1, 2 * start_y + 1, CellType.ROAD)
    checklist = [(start_x, start_y)]
    while len(checklist):
        entry = choice(checklist)
        if not check_neighbors(map, entry[0], entry[1], width, height, checklist):
            checklist.remove(entry)


def do_random_prime(map):
    map.reset_maze(CellType.WALL) #全部设为墙
    random_prime(map, (map.width - 1) // 2, (map.height - 1) // 2) #size = m * 2 - 1，此处使用(map,m,m)


def set_entrance_exit(maze):
    entrance = []
    for i in range(maze.height):
        if maze.maze[i][1] == 0: #设置开始点，左上角
            maze.set_maze(0, i, 0)
            entrance = [0, i]
            break
    exit = [] #设置结束点，右下角
    for i in range(maze.height - 1, 0, -1):
        if maze.maze[i][maze.width - 2] == 0:
            maze.set_maze(maze.width - 1, i, 0)
            exit = [maze.width - 1, i]
            break
    return entrance, exit


def generate_maze(width, height):
    # 初始化迷宫
    maze = Maze(width, height) #size = m * 2 + 1
    # 生成地图
    do_random_prime(maze)
    # 选择起点和终点
    entrance, exit = set_entrance_exit(maze)
    # 返回地图
    return maze.maze, entrance, exit

