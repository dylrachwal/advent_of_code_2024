import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help='input file')
    args = parser.parse_args()
    return args

def parse_input(input:str):
    with open(input, "r", encoding="utf-8") as f:
        orders, updates = f.read().split('\n\n')
    return generate_orders(orders), parse_updates(updates)

def generate_orders(orders):
    couples = orders.split('\n')
    order_dict = {}
    for couple in couples:
        before, after = couple.split('|')
        before , after = int(before), int(after)
        if not(before in order_dict.keys()):
            order_dict[before] = {after}
        else:
            order_dict[before].add(after)
    return order_dict

def parse_updates(updates):
    updates = updates.split('\n')
    res = []
    for update in updates:
        res.append(list(map(int, update.split(','))))
    return res

def sum_correct(orders, updates):
    res = 0
    for update in updates:
        n = len(update)
        correct = [update[0]]
        for idx, page in enumerate(update[1:]):
            intersect = orders[page].intersection(correct)
            if intersect:
                min_ind = 1000000000000000000000
                for after_page in intersect:
                    min_ind = min(correct.index(after_page), min_ind)
                correct.insert(min_ind, page)
                break
            else:
                correct.append(page)
        res += correct[n//2] if len(correct) == n else 0
    return res


if __name__ == '__main__':
    args = parse_args()
    orders, updates = parse_input(args.input)
    print(sum_correct(orders, updates))