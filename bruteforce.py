class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

class List_of_Actions:
    def __init__(self, list_of_actions: list[Action]):
        self.list_of_actions = list_of_actions

    def subset_sum(self, numbers, target, results, partial=[]):
        s = 0
        for each in partial:
            if isinstance(each, Action):
                s += each.price

        if s == target:
            results.append(partial)
        if s >= target:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            self.subset_sum(remaining, target, results, partial + [n])

    def profit_eval(self):
        results = []
        target = 500
        self.subset_sum(self.list_of_actions, target, results)
        
        maximum_profit = 0
        maximum_result = None
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
    my_list = List_of_Actions(
        [
            Action("Action-1", 20, 5),
            Action("Action-2", 30, 10),
            Action("Action-3", 50, 15),
            Action("Action-4", 70, 20),
            Action("Action-5", 60, 17),
            Action("Action-6", 80, 25),
            Action("Action-7", 22, 7),
            Action("Action-8", 26, 11),
            Action("Action-9", 48, 13),
            Action("Action-10", 34, 27),
            Action("Action-11", 42, 17),
            Action("Action-12", 110, 9),
            Action("Action-13", 38, 23),
            Action("Action-14", 14, 1),
            Action("Action-15", 18, 3),
            Action("Action-16", 8, 8),
            Action("Action-17", 4, 12),
            Action("Action-18", 10, 14),
            Action("Action-19", 24, 21),
            Action("Action-20", 114, 18),
        ]
    )
    
    maximum_result, maximum_profit = my_list.profit_eval()
    
    for action in maximum_result:
        print(action.__dict__)
    print(f"Maximum profit is {maximum_profit}")