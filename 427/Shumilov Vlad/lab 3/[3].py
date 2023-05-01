

with open('maze-for-u.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


# for i in range(len(maze)):
#     for j in range(len(maze[0])):
#         if maze[i][j] == "*":
#             key = (i, j)
#             maze[i][j] = " "
#             break

# for Y in range(len(maze[0])):
#     if maze[0][Y] == " ":
#         start = (0, Y)
#         break


def dfs(coordsX, coordsY, visited):
    LenMazeY = len(maze[0])
    LenMazeX = len(maze)

    # проверяем, не достигли ли мы выхода
    if maze[coordsX][coordsY] == "*" and (coordsX, coordsY) not in visited:
        print("Выход найден!")
        return [(coordsX, coordsY)]

    # добавляем текущую позицию в список посещенных
    visited.append((coordsX, coordsY))

    # проверяем все возможные направления движения
    if (coordsX - 1) >= 0 and maze[coordsX - 1][coordsY] == " " and (coordsX - 1, coordsY) not in visited:
        path = dfs(coordsX - 1, coordsY, visited)
        if path:
            return [(coordsX, coordsY)] + path

    if (coordsX + 1) < LenMazeX and maze[coordsX + 1][coordsY] == " " and (coordsX + 1, coordsY) not in visited:
        path = dfs(coordsX + 1, coordsY, visited)
        if path:
            return [(coordsX, coordsY)] + path

    if (coordsY - 1) >= 0 and maze[coordsX][coordsY - 1] == " " and (coordsX, coordsY - 1) not in visited:
        path = dfs(coordsX, coordsY - 1, visited)
        if path:
            return [(coordsX, coordsY)] + path

    if (coordsY + 1) < LenMazeY and maze[coordsX][coordsY + 1] == " " and (coordsX, coordsY + 1) not in visited:
        path = dfs(coordsX, coordsY + 1, visited)
        if path:
            return [(coordsX, coordsY)] + path

    # если выход не найден, удаляем текущую позицию из списка посещенных и возвращаем пустой список
    visited.pop()
    return []

pathToKey = dfs(0, 1, [])
print(pathToKey)
for coords in pathToKey:
    x, y = coords
    maze[x][y] = "."

# with open('maze-for-me-done.txt', 'w') as f:
#     for line in maze:
#         f.write("".join(line) + "\n")
