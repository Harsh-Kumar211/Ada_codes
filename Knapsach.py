def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratio.sort(reverse=True)  

    total_value = 0
    total_weight = 0
    for r, w, v in ratio:
        if total_weight + w <= capacity:
            total_value += v
            total_weight += w
        else:
            fraction = (capacity - total_weight) / w
            total_value += fraction * v
            break 
    return total_value

def main():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []
    for i in range(n):
        weight = int(input(f"Enter weight of item {i+1}: "))
        value = int(input(f"Enter value of item {i+1}: "))
        weights.append(weight)
        values.append(value)
    capacity = int(input("Enter the capacity of knapsack: "))
    print("Maximum value using greedy algorithm:", knapsack_greedy(weights, values, capacity))

if __name__ == "__main__":
    main()
