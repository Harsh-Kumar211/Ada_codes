def optimal_bst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            freq_sum = sum(freq[i:j+1])

            for r in range(i, j + 1):
                c = cost[i][r - 1] + (cost[r + 1][j] if r < j else 0) + freq_sum
                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]

# Input from the user
n = int(input("Enter the number of keys: "))
keys = []
freq = []
for i in range(n):
    key = int(input("Enter key {}: ".format(i + 1)))
    keys.append(key)
    f = int(input("Enter frequency for key {}: ".format(i + 1)))
    freq.append(f)

print("Cost of optimal binary search tree:", optimal_bst(keys, freq))
