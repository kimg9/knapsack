# Stock Investment Profit Calculator
## Overview
This project implements a dynamic programming solution to the Knapsack problem, specifically tailored for stock investment analysis. The goal is to help investors determine the optimal combination of stocks to purchase from various companies, maximizing profit over a two-year period.

# Problem Statement
Given a list of companies, each with associated stock prices and projected profits over two years, the task is to determine the best investment strategy. This involves selecting stocks while adhering to a budget constraint to maximize overall profit.

## Brute force vs Optimized solution
* **Dynamic Programming Approach**: Efficiently solves the Knapsack problem using a bottom-up dynamic programming technique with a time complexity of 𝑂(𝑛×𝐵), where 𝑛 is the number of stocks and 𝐵 is the budget.
* **Brute Force Solution**: the repo includes a brute force method for comparison, with a time complexity of 𝑂(2𝑛), providing a baseline for understanding the performance gains achieved through optimization.

## Example
Given the following stock data:

| Company     | Price | Profit |
|:-----------:|------:|:------:|
| Stock A     |   100 |    20% |
| Stock B     |   200 |     3% |
| Stock C     |   150 |   4.5% |
If the budget is €200, the output will provide the optimal stocks to purchase and the maximum profit achievable over the two years.

## Algorithm Explanation
This solution employs a dynamic programming approach to tackle the Knapsack problem:

* Initialization: A 2D array is created to store maximum profits for different capacities and items.
* Iteration: The algorithm iteratively calculates the maximum profit for each item and capacity.
* Backtracking: After populating the array, the optimal stock choices are derived through backtracking.

## Acknowledgments
* [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
* [Knapsack Problem])(https://en.wikipedia.org/wiki/Knapsack_problem)
