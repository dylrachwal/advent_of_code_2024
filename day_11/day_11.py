import argparse
import time

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    with open(input, "r", encoding="utf-8") as f:
        return list(map(int,f.read().split(" ")))

def blinks(stones, nb_blinks):
    counter = 0
    current_stones = stones
    while(counter < nb_blinks):
        next_stones = []
        for stone_value in current_stones:
            str_stone_value = str(stone_value)
            n =  len(str_stone_value)
            if stone_value == 0:
                next_stones.append(stone_value + 1)
            elif n % 2 == 0:
                next_stones += [int(str_stone_value[:n//2]), int(str_stone_value[n//2:])]
            else:
                next_stones.append(stone_value * 2024)
        current_stones = next_stones
        counter += 1
    print(len(current_stones))

def blinks_optimized(stones, nb_blinks):
    counter = 0
    current_stones = {}
    for stone in stones:
        current_stones[stone] = current_stones.get(stone, 0) + 1
    while(counter < nb_blinks):
        next_stones = {}
        for stone_value, appeareance in current_stones.items():
            str_stone_value = str(stone_value)
            n =  len(str_stone_value)
            if stone_value == 0:
                next_stones[1] = next_stones.get(1, 0) + appeareance
            elif n % 2 == 0:
                next_stones[int(str_stone_value[:n//2])] = next_stones.get(int(str_stone_value[:n//2]), 0) + appeareance
                next_stones[int(str_stone_value[n//2:])] = next_stones.get(int(str_stone_value[n//2:]), 0) + appeareance
            else:
                 next_stones[stone_value*2024] = next_stones.get(stone_value*2024, 0) + appeareance
        current_stones = next_stones
        counter += 1
    print(sum(current_stones.values()))


if __name__ == '__main__':
    args = parse_args()
    stones = parse_input(args.input)
    blinks(stones, 25)
    start_time = time.time()
    blinks_optimized(stones, 75)
    print(time.time() - start_time)