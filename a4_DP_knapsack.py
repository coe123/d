import numpy as np

def print_T_arr(T_arr, n, mw):
    # Printing column headers
    print(" |", end="")
    for i in range(mw + 1):
        print(f"{i:5}", end="")
    print("\n" + "-" * (6 * (mw + 2)))
    
    for i in range(n + 1):
        print(f"{i:2}|", end="")
        for j in range(mw + 1):
            print(f"{T_arr[i, j]:5}", end="")
        print()

def knapsack_01(profit_arr, weight_arr, n, mw):
    T_arr = np.zeros((n + 1, mw + 1), dtype=int)
    
    for i in range(1, n + 1):
        for j in range(mw + 1):
            if weight_arr[i - 1] <= j:
                T_arr[i, j] = max(T_arr[i - 1, j], profit_arr[i - 1] + T_arr[i - 1, j - weight_arr[i - 1]])
            else:
                T_arr[i, j] = T_arr[i - 1, j]
    
    print("DP Table:")
    print_T_arr(T_arr, n, mw)
    
    # Finding the items included
    included = np.zeros(n, dtype=bool)
    j = mw
    for i in range(n, 0, -1):
        if T_arr[i, j] != T_arr[i - 1, j]:
            included[i - 1] = True
            j -= weight_arr[i - 1]
    
    max_profit = T_arr[n, mw]
    return max_profit, included

def inputing():
    print("Enter the max weight capacity: ")
    mw = int(input())
    print("Enter number of objects: ")
    n = int(input())
    
    profit_arr = []
    weight_arr = []
    
    for i in range(n):
        print(f"Enter profit of object number {i+1}: ")
        profit = int(input())
        profit_arr.append(profit)
        
        print(f"Enter weight of object number {i+1}: ")
        weight = int(input())
        weight_arr.append(weight)
    
    max_profit, included = knapsack_01(profit_arr, weight_arr, n, mw)
    
    print(f"\nMaximum Profit: {max_profit}")
    print("Included items: ", included.astype(int))

inputing()
