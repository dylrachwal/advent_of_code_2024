import argparse

moves = [(-1,0), (0,1), (1,0), (0,-1)]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    with open(input, "r", encoding="utf-8") as f:
        return [list(map(int,line.strip())) for line in f.readlines()]

def is_in_bound(limit_x, limit_y, x, y):
    return 0 <= x < limit_x and 0 <= y < limit_y

def score_trailheads(matrix):
    trailheads = {}
    score = 0
    rate = 0
    max_x, max_y =  len(matrix), len(matrix[0])
    for x in range(max_x):
        for y in range(max_y):
            if matrix[x][y] == 0:
                trailheads[(x, y)] = 0
    queue = [trailhead for trailhead in trailheads]
    trailends = set()
    while queue:
        x, y = queue.pop()
        if matrix[x][y] == 0:
            score += len(trailends)
            trailends = set()
        for (dx, dy) in moves:
            next_x, next_y = x + dx, y + dy
            if(is_in_bound(max_x, max_y, next_x, next_y)):
                current, next = matrix[x][y], matrix[next_x][next_y]
                if next - current == 1:   
                    if next == 9:
                        rate+=1
                        trailends.add((next_x, next_y))
                    else:
                        queue += [(next_x, next_y)]
    score += len(trailends)
    print(rate)
    print(score)
    return trailheads

if __name__ == '__main__':
    args = parse_args()
    matrix = parse_input(args.input)
    print(rate_trailheads(matrix))