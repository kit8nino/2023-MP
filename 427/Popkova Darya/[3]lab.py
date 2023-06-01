from collections import deque

wall, path = 1, 0

def maze_to_matrix(input_maze_file="maze-for-u.txt"):
    M = []
    with open(input_maze_file,"r") as f:
        for line in f:
            M.append(list(line)[:-1])
    height = len(M)
    width = len(M[0])
    for i in range(height):
        for j in range(width):
            M[i][j] = wall if M[i][j] == '#' else path
    return M, width, height

Matrix, Matrix_width, Matrix_heigth = maze_to_matrix()

def start_avatar_coord():
    a_x = int(input("Enter x start avatar coord: "))
    a_y = 0
    if Matrix[a_y][a_x] == wall:
        for i in range(Matrix_width):
            if Matrix[a_y][i] == path:
                a_x = i
    return a_x, a_y

(Avatar_start_coord_x, Avatar_start_coord_y) = start_avatar_coord()

def key_coord():
    k_x = int(input("Enter x key coord: "))
    k_y = int(input("Enter y key coord: "))
    break_flg = False
    if Matrix[k_y][k_x] == wall:
        for i in range(k_y, Matrix_heigth):
            for j in range(k_x, Matrix_width):
                if Matrix[i][j] == path:
                    break_flg = True
                    k_y = i
                    k_x = j
                    break
            if break_flg: break
        else:
            break_flg = False
            for i in range(k_y, 0, -1):
                for j in range(k_x,0,-1):
                    if Matrix[i][j] == path:
                        break_flg = True
                        k_y = i
                        k_x = j
                        break
                if break_flg: break
    return k_x, k_y

(Key_x, Key_y) = key_coord()

def exit_coord():
    e_x = int(input("Enter x exit coord: "))
    e_y = Matrix_heigth - 1
    if Matrix[e_y][e_x] == wall:
        for i in range(Matrix_width):
            if Matrix[e_y][i] == path:
                e_x = i
    return e_x, e_y

(Exit_x, Exit_y) = exit_coord()

def bfs_to(M, s, e):
    n = Matrix_heigth
    m = Matrix_width
    const = 10 ** 10
    delt = [(0,-1),(0,1),(1,0),(-1,0)]
    d = [[const] * m for _ in range(n)]
    p = [[None] * m for _ in range(n)]

    used = [[False] * m for _ in range(n)]
    queue = deque()

    d[s[0]][s[1]] = 0
    used[s[0]][s[1]] = True
    queue.append(s)

    while len(queue) != 0:
        x, y = queue.popleft()
        for dx, dy in delt:
            nx, ny = x + dx, y + dy
            if 0 < nx < n and 0 < ny < m and not used[nx][ny] and M[nx][ny] != '#':
                d[nx][ny] = d[x][y] + 1
                p[nx][ny] = (x, y)
                used[nx][ny] = True 
                queue.append((nx, ny))
    cur = e
    path = []
    while cur is not None:
        path.append(cur)
        cur = p[cur[0]][cur[1]]
    path.reverse()
    return path
    
path1 = bfs_to(Matrix, (Avatar_start_coord_y, Avatar_start_coord_x), (Key_y, Key_x))[:-1]
path2 = bfs_to(Matrix, (Key_y, Key_x), (Exit_y, Exit_x))[1:]

key, visited_1, visited_2 = 2, 3, 4
Matrix[Key_y][Key_x] = key

print(path1)

for y,x in path1:
    Matrix[y][x] = visited_1
for y,x in path2:
    Matrix[y][x] = visited_2

def draw(file="maze-for-me-done.txt"):
    d = {wall: '#', path: ' ' ,visited_1: '.', visited_2: ',', key: '*'}
    with open(file, 'w') as f:
        for i in range(Matrix_heigth):
            for j in range(Matrix_width):
                if Matrix[i][j] == wall: f.write(d[wall])
                elif Matrix[i][j] == path: f.write(d[path])
                elif Matrix[i][j] == key: f.write(d[key])
                elif Matrix[i][j] == visited_1: f.write(d[visited_1])
                elif Matrix[i][j] == visited_2: f.write(d[visited_2]) 

draw()