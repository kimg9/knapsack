from itertools import combinations
import csv

class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit


class List_of_Actions:
    def __init__(self, list_of_actions: list[Action]):
        self.list_of_actions = list_of_actions
    
    # def manual_possibilities_to_target(self, numbers, target, results, partial=[]):
    #     s = 0
    #     for each in partial:
    #         if isinstance(each, Action):
    #             s += each.price
    #     if s <= target:
    #         results.append(partial)
    #     if s >= target:
    #         return
    #     for i in range(len(numbers)):
    #         n = numbers[i]
    #         remaining = numbers[i + 1:]
    #         self.manual_possibilities_to_target(remaining, target, results, partial + [n])
    
    def find_all_sets_to_target(self, target):
        all_possibilities = []
        for count in range(1, len(self.list_of_actions)):
            for actions_combination in combinations(self.list_of_actions, count):
                if sum(action.price for action in actions_combination) <= target:
                    all_possibilities.append(actions_combination)
        return all_possibilities

    def find_maximum_profit_set(self):
        target = 500
        # results = []
        # self.all_possibilities_equal_to_target(self.list_of_actions, target, results)
        results = self.find_all_sets_to_target(target)
        
        maximum_profit = 0
        maximum_result = []
        for result in results:
            total_profit = 0
            for action in result:
                total_profit += action.price + (action.price * action.profit / 100)
            if total_profit > maximum_profit:
                maximum_profit = total_profit
                maximum_result = result
            else:
                continue
        
        return maximum_result, maximum_profit
            

if __name__ == "__main__":
    with open('datasets/liste_actions.csv') as file:
        reader = csv.reader(file)
        next(reader, None) #skip header
        list_of_actions = []
        for row in reader:
            list_of_actions.append(Action(row[0], int(row[1]), int(row[2].strip("%"))))
            
        my_list = List_of_Actions(list_of_actions=list_of_actions)
    
    maximum_result, maximum_profit = my_list.find_maximum_profit_set()
    
    for action in maximum_result:
        print(action.__dict__)
    print(f"Maximum profit is {round(maximum_profit, 2)}")
    print(f"Invested amount is {sum(action.price for action in maximum_result)}")