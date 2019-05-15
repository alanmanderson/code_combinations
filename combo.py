import argparse

graph = {
    1: {'right':[2,3], 'down':[4,7]},
    2: {'left':[1],'right':[3], 'down':[2,5,8,0]},
    3: {'left':[1,2], 'down':[6,9]},
    4: {'up': [1], 'right':[5,6], 'down': [7]},
    5: {'up': [2], 'right':[6], 'down': [8,0], 'left': [4]},
    6: {'up': [3], 'down': [9], 'left': [5,4]},
    7: {'up': [4,1], 'right': [8,9]},
    8: {'up': [5,2], 'right': [9], 'down':[0], 'left': [7]},
    9: {'up': [6,3], 'left': [8,7]},
    0: {'up': [8,5,2]}
}

def possible_combos(shape):
    combos = []
    queue = [{'path':[x], 'shape': shape.copy()} for x in range(10)]
    path = []
    while len(queue) > 0:
        cur_state = queue.pop(0)
        cur_direction = cur_state['shape'].pop(0)
        new_locations = graph[cur_state['path'][-1]].get(cur_direction, [])
        for location in new_locations:
            cur_path = cur_state['path'].copy() + [location]
            if len(cur_state['shape']) == 0:
                combos.append(cur_path)
                continue
            queue.append({'path':cur_path,'shape':cur_state['shape'].copy()})
    return combos

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='identify potential combos')
    parser.add_argument('pattern', type=str, nargs='+', help='type a list of directions separated by a space.  Like this: up down left right')
    args = parser.parse_args()
    combos = possible_combos(args.pattern)

print("There are a total of {} combos".format(len(combos)))
print(combos)

