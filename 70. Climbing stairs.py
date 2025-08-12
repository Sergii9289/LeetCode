def find_combinations(n):
    result = []

    def backtrack(current, total):
        if total == n:
            result.append(current[:])
            return
        if total > n:
            return

        current.append(1)
        backtrack(current, total + 1)
        current.pop()

        current.append(2)
        backtrack(current, total + 2)
        current.pop()

    backtrack([], 0)
    return result

#-----------------------------------------------------------------------------

def count_combinations(n):
    count = 0

    def backtrack(total):
        nonlocal count
        if total == n:
            count += 1
            return
        if total > n:
            return

        backtrack(total + 1)
        backtrack(total + 2)

    backtrack(0)
    return count

#-----------------------------------------------------------------------------------------

n = 10

for combo in find_combinations(n):
    print(combo)
print(f'Кількість комбінацій для {n} сходинок - {count_combinations(n)}')  # Виведе: 5


#--------------dynamic programming---------------------------------------------------------

def dynamic_count_combinations(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 2 >= 0:
            dp[i] += dp[i - 2]

    return dp[n]

print(f'Динамічний пошук для {n} сходинок - {dynamic_count_combinations(n)}')