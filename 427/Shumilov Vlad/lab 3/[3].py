

with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == "*":
            key = (i, j)
            print(key)
            maze[i][j] = " "
            break


for Y in range(len(maze[0])):
    if maze[0][Y] == " ":
        start = (0, Y)
        break


def dfs(start, end, maze):
    LenMazeY = len(maze[0])
    LenMazeX = len(maze)
    stack = [start]
    visited = [start]
    while stack:
        current_pos = stack.pop()
        if current_pos == end:
            return visited

        coordsX, coordsY = current_pos

        # проверяем все возможные направления движения
        if (coordsX - 1) >= 0 and maze[coordsX - 1][coordsY] == " " and (coordsX - 1, coordsY) not in visited:
            stack.append((coordsX - 1, coordsY))
            visited.append((coordsX - 1, coordsY))

        if (coordsX + 1) < LenMazeX and maze[coordsX + 1][coordsY] == " " and (coordsX + 1, coordsY) not in visited:
            stack.append((coordsX + 1, coordsY))
            visited.append((coordsX + 1, coordsY))

        if (coordsY - 1) >= 0 and maze[coordsX][coordsY - 1] == " " and (coordsX, coordsY - 1) not in visited:
            stack.append((coordsX, coordsY - 1))
            visited.append((coordsX, coordsY - 1))

        if (coordsY + 1) < LenMazeY and maze[coordsX][coordsY + 1] == " " and (coordsX, coordsY + 1) not in visited:
            stack.append((coordsX, coordsY + 1))
            visited.append((coordsX, coordsY + 1))
    return None


pathToKey = dfs(start, key, maze)

for coords in pathToKey:
    x, y = coords
    maze[x][y] = "."

with open('maze-for-me-done.txt', 'w') as f:
    for line in maze:
        f.write("".join(line) + "\n")
