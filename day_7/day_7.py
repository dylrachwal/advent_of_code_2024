import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    equations = []
    with open(input, "r", encoding="utf-8") as f:
        for line in f:
            temp = line.split(": ")
            equations.append((int(temp[0]),list(map(int,temp[1].split(" ")))))
    return equations

def get_calibration(equations, part_2 = False):
    calibration = 0
    for equation in equations:
        test_value, values = equation
        results = set()
        for i in range(len(values)):
            new_set = set()
            if results:
                for result in results:
                    new_set.add(result + values[i])
                    new_set.add(result * values[i])
                    if part_2:
                        new_set.add(int(str(result)+str(values[i])))
            else:
                new_set.add(values[i])
            results = new_set
        print(f"test value {test_value} for values {values} was {test_value in results}")
        calibration += test_value if test_value in results else 0
    return calibration

if __name__ == '__main__':
    args = parse_args()
    equations = parse_input(args.input)
    print(get_calibration(equations))
    print(get_calibration(equations, True))