actions = [100,20,30,50,70,60,80,22,26,48,34]
target = 100
working = []

def search(start, previous_values, current_combination):
    print(current_combination)
    while len(actions[start:]) != 0:
        for i, v in enumerate(actions[start:]):
            if previous_values + v == target:
                current_combination.append(v)
                return current_combination
            elif previous_values + v > target:
                return current_combination
            elif previous_values + v < target:
                current_combination.append(previous_values)
                search(i, v, current_combination)

for index, action in enumerate(actions):
    if action == target:
        working.append(action)
        continue
    else:
        result = search(index, 0, [])
        working.append(result)
        
print(working)