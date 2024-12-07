import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    matrix = []
    with open(input, "r", encoding="utf-8") as f:
        matrix= ([line.strip() for line in f.readlines()])
    return matrix

def is_in_bound(limit_x, limit_y, x, y):
    return 0 <= x < limit_x and 0 <= y < limit_y

def search_word(word, matrix):
    vector = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    delta = len(word)
    ### assuming it s a rectangle
    n=len(matrix)
    m=len(matrix[0])
    count = 0
    for x in range(n):
        for y in range(m):
            for dx, dy in vector:
                if not is_in_bound(n,m,x+(delta-1)*dx, y+(delta-1)*dy):
                    continue
                match = 1
                for i in range(delta):
                    if matrix[x+i*dx][y+i*dy]!= word[i]:
                        match = 0
                        break
                count += match
    return count


def x_mas(matrix):
    diags = [[(1, -1), (-1, 1)], [(1, 1), (-1, -1)]]
    n=len(matrix)
    m=len(matrix[0])
    count = 0
    for x in range(1,n-1):
        for y in range(1,m-1):
            if matrix[x][y]!='A':
                continue
            match = 0
            for diag in diags:
                letters = {matrix[x+coord[0]][y+coord[1]] for coord in diag}
                if letters == {'M', 'S'}:
                    match += 1
            count += 1 if match == len(diags) else 0
    return count



if __name__ == '__main__':
    args = parse_args()
    matrix = parse_input(args.input)
    print(search_word('XMAS', matrix))
    print(x_mas(matrix))