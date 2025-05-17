import argparse
from copy import deepcopy

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str, test = False):
    if test:
        return list(map(int, input))
    with open(input, "r", encoding="utf-8") as f:
        return list(map(int, f.read()))

def expand_diskmap(diskmap):
    res = []
    for i in range(len(diskmap)):
        value = i//2 if i % 2 == 0 else "."
        res += [value] * diskmap[i]
    return res

def reorder_diskmap(expanded_diskmap):
    res = deepcopy(expanded_diskmap)
    while res.count("."):
        first_empty_space = res.index(".")
        last_file = res.pop()
        res[first_empty_space] = last_file
        while res[-1] == ".":
            res.pop()
    return res

def checksum(reordered_diskmap):
    return sum(i*value for i, value in enumerate(reordered_diskmap))

def separate_free_space_and_files(diskmap):
    free_spaces, files = [], []
    first_space = 0
    for i in range(len(diskmap)):
        space = diskmap[i]
        if i % 2 == 0:
            files.append((first_space, space, i//2))
        else:
            free_spaces.append((first_space, space))
        first_space +=space
    return free_spaces, files

def move_files(files, free_spaces):
    for i in range(len(files)-1, -2, -1):
        file_position, file_space, ind = files[i]
        for j in range(len(free_spaces)):
            free = free_spaces[j]
            free_position, free_space = free
            if free_position < file_position and free_space >= file_space:
                files[i] = (free_position, file_space, ind)
                free_spaces[j] = (free_position + file_space, free_space - file_space)
                break

def checksum_part_2(files):
    res = 0
    for file in files:
        pos, space, ind = file
        for i in range(space):
            res += (pos + i) * ind
    return res

if __name__ == '__main__':
    args = parse_args()
    diskmap = parse_input(args.input)
    free, files = separate_free_space_and_files(diskmap)
    move_files(files, free)
    print(files)
    print(checksum_part_2(files))