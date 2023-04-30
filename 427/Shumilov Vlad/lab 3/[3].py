with open('test-maze.txt', 'r') as f:
    maze = [list(line.strip()) for line in f.readlines()]


def get_empty_cells(coord, maze):
    width = len(maze[0])
    height = len(maze)
    x_coord = coord[0]
    y_coord = coord[1]
    possibles = []

