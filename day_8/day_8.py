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

def get_antennas(matrix):
    antennas = set()
    antennas_per_freq = {}
    for x, line in enumerate(matrix):
        for y, value in enumerate(line):
            if value != '.':
                if value not in antennas_per_freq:
                    antennas_per_freq[value] = []
                antennas_per_freq[value].append((x, y))
                antennas.add(value)
    return (antennas_per_freq,antennas)

def count_antinodes(matrix, antennas, antennas_per_freq):
    res = 0
    max_x = len(matrix)
    max_y = len(matrix[0])
    for _, pos in antennas_per_freq.items():
        n = len(pos)
        if(n == 1):
            continue
        for i in range(n-1):
            for j in range(i+1, n):
                x_1,y_1 = pos[i]
                x_2,y_2 = pos[j]
                dx = x_2 - x_1
                dy = y_2 - y_1
                antinode_1_x, antinode_1_y = x_1 - dx, y_1 - dy
                antinode_2_x, antinode_2_y = x_2 + dx, y_2 + dy
                if ((antinode_1_x, antinode_1_y) not in antennas and is_in_bound(max_x, max_y, antinode_1_x, antinode_1_y)):
                    antennas.add(((antinode_1_x, antinode_1_y) ))
                    res += 1
                if ((antinode_2_x, antinode_2_y) not in antennas and is_in_bound(max_x, max_y, antinode_2_x, antinode_2_y)):
                    antennas.add(((antinode_2_x, antinode_2_y) ))
                    res += 1
    return res

def count_harmonic(matrix, antennas_per_freq):
    max_x = len(matrix)
    max_y = len(matrix[0])
    harmonics = set()
    for _, pos in antennas_per_freq.items():
        n = len(pos)
        if(n == 1):
            continue
        for i in range(n-1):
            for j in range(i+1, n):
                x_1,y_1 = pos[i]
                x_2,y_2 = pos[j]
                dx = x_2 - x_1
                dy = y_2 - y_1
                antinode_1_x, antinode_1_y = x_1, y_1
                while (is_in_bound(max_x, max_y, antinode_1_x, antinode_1_y)):
                    harmonics.add((antinode_1_x, antinode_1_y))
                    antinode_1_x -= dx
                    antinode_1_y -= dy
                antinode_2_x, antinode_2_y = x_2, y_2
                while (is_in_bound(max_x, max_y, antinode_2_x, antinode_2_y)):
                    harmonics.add((antinode_2_x, antinode_2_y))
                    antinode_2_x += dx
                    antinode_2_y += dy
    return len(harmonics)

if __name__ == '__main__':
    args = parse_args()
    matrix = parse_input(args.input)

    antennas_per_freq, antennas = get_antennas(matrix)
    print(count_antinodes(matrix, antennas, antennas_per_freq))
    print(count_harmonic(matrix, antennas_per_freq))