def knapsack(values, weights, capacity):
    n = len(values)
    # Create a table to store the maximum value that can be obtained
    # with the first i items and a knapsack capacity j
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # If the current item can fit into the knapsack
            if weights[i - 1] <= j:
                # Choose the maximum value between including the item
                # or excluding the item
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                # If the current item cannot fit, exclude it
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]

# Function to take input from the user
def take_input():
    n = int(input("Enter the number of items: "))
    values = []
    weights = []
    for i in range(n):
        value = int(input("Enter value for item {}: ".format(i + 1)))
        weight = int(input("Enter weight for item {}: ".format(i + 1)))
        values.append(value)
        weights.append(weight)
    capacity = int(input("Enter the capacity of the knapsack: "))
    return values, weights, capacity

# Main function
def main():
    values, weights, capacity = take_input()
    max_value = knapsack(values, weights, capacity)
    print("Maximum value:", max_value)

if __name__ == "__main__":
    main()
