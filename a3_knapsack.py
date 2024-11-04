def knapsack(val, weights, capacity):
    n = len(val)
    dp = [[0 for _ in range(capacity + 1)] for _ in range (n+1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + val[i - 1])
            else :
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items  :"))
val = []
weights = []

print("Enter the values of the items : ")
for i in range(n):
    value = int(input(f"Enter value of item {i+1}"))
    val.append(value)

print("Enter the weights of the items : ")
for i in range(n):
    weight = int(input(f"Enter value of item {i+1}"))
    weights.append(weight)

capacity = int(input("Enter the capacity of knapsack : "))

print("Maximum capacity of knapsack is : ", knapsack(val, weights, capacity))
