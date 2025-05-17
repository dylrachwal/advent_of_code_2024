import argparse

directions = ['^', '>', 'v', '<']
moves = [(-1,0), (0,1), (1,0), (0,-1)]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    matrix = []
    with open(input, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def search_guard(matrix):
    for i, line in enumerate(matrix):
        for j, pos in enumerate(line):
            if pos in directions:
                return (i, j)
    return (-1, -1)

def nb_loop(matrix, init):
    s = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == '.':
                matrix[x] = matrix[x][:y] + '#' + matrix[x][y+1:]
                _, is_loop = visit_map(matrix, init)
                if is_loop:
                    print(f"found loop at {x}{y}")
                s += 1 if is_loop else 0
                matrix[x] = matrix[x][:y] + '.' + matrix[x][y+1:]
    return s

def visit_map(matrix, init):
    visited_map = set()
    visited_map_dir = set()
    guard = init
    direction = directions.index(matrix[guard[0]][guard[1]])
    max_x, max_y = len(matrix), len(matrix[0])
    is_loop=False
    while True:
        visited_map.add(guard)
        if ((guard, (direction)% 4)) in visited_map_dir:
            is_loop = True
            break
        visited_map_dir.add((guard, direction))
        move = moves[direction]
        next = (guard[0] + move[0], guard[1] + move[1])
        if not(0 <= next[0]<max_x and 0 <= next[1]<max_y) :
            guard = next
            break
        if matrix[next[0]][next[1]] == "#":
            direction = (direction + 1) % 4
        else:
            guard = next
    return len(visited_map), is_loop

if __name__ == '__main__':
    args = parse_args()
    matrix = parse_input(args.input)
    init = search_guard(matrix)
    print(nb_loop(matrix, init))