import argparse
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

    @staticmethod
    def dynamic_programming(budget: int, cost, profit):
        """
        Calculate the maximum profit and return the generated table.

        :param cost: List of costs of the actions
        :param profit: List of profit of the actions
        :param budget: Maximum budget
        :return: Maximum profit and the filled table
        """
        n = len(profit)
        table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(budget + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif cost[i - 1] <= j:
                    table[i][j] = max(
                        profit[i - 1] + table[i - 1][j - cost[i - 1]], table[i - 1][j]
                    )
                else:
                    table[i][j] = table[i - 1][j]

        return table[n][budget], table

    @staticmethod
    def find_included_items(cost, table):
        """
        Find the items included in the optimal solution based on the table.

        :param cost: List of cost of the items
        :param table: table computed by dynamic_programming
        :return: List of included items (1-based index)
        """
        n = len(cost)
        B = len(table[0]) - 1
        included_items = []
        i, j = n, B

        while i > 0 and j > 0:
            if table[i][j] != table[i - 1][j]:
                included_items.append(i)
                j -= cost[i - 1]
            i -= 1

        included_items.reverse()
        return included_items


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="csv file to analyze")
    args = parser.parse_args()

    if args.csv:
        with open(args.csv, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            list_of_actions = []
            for row in reader:
                action_name = row[0]
                action_price = float(row[1]) if 0 < float(row[1]) <= 500 else 0
                if not action_price:
                    continue
                action_profit = action_price * float(row[2].strip("%")) / 100
                list_of_actions.append(Action(action_name, action_price, action_profit))

        my_list = List_of_Actions(list_of_actions=list_of_actions)
        file.close()

        all_costs = [int(x.price * 100) for x in my_list.list_of_actions]
        all_profits = [int(x.profit * 100) for x in my_list.list_of_actions]
        result, table = my_list.dynamic_programming(
            500 * 100,
            all_costs,
            all_profits,
        )

        included_items = my_list.find_included_items(all_costs, table)
        actual_actions_included = []

        print("The optimized algorithm bought:")

        for index, action in enumerate(my_list.list_of_actions):
            if index + 1 in included_items:
                actual_actions_included.append(action)
                print(action.name)

        print(f"Total cost: {sum([x.price for x in actual_actions_included])}")
        print(f"Total return: {round(result, 2)/100}")
