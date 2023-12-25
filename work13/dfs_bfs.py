maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
from collections import deque

def bfs(maze, start, end):
    queue = deque([start])
    visited = set()
    parent = {}
    found = False

    while queue:
        current = queue.popleft()
        if current == end:
            found = True
            break

        for next_move in get_neighbors(current, maze):
            if next_move not in visited:
                queue.append(next_move)
                visited.add(next_move)
                parent[next_move] = current

    if found:
        path = []
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path
    else:
        return None

def get_neighbors(cell, maze):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        x, y = cell[0] + dx, cell[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            neighbors.append((x, y))
    return neighbors

start = (0, 0)
end = (4, 4)
bfs_path = bfs(maze, start, end)
print(bfs_path)
def dfs(maze, start, end):
    stack = [start]
    visited = set()
    parent = {}
    found = False

    while stack:
        current = stack.pop()
        if current == end:
            found = True
            break

        for next_move in get_neighbors(current, maze):
            if next_move not in visited:
                stack.append(next_move)
                visited.add(next_move)
                parent[next_move] = current

    if found:
        path = []
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path
    else:
        return None

start = (0, 0)
end = (4, 4)
dfs_path = dfs(maze, start, end)
print(dfs_path)
