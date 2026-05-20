"""
Day81 :- Fibonacci using Dynamic Programming
Difficulty :- Easy
Concepts :- DP, memoization, tabulation
"""
def fibonacci_top_down(n, memo=None):
    """Top-Down DP"""
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    return memo[n]


def fibonacci_bottom_up(n):
    """Bottom-Up DP """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

while True:
    print("\n===== Fibonacci Using Dynamic Programming =====")
    print("1. Fibonacci using Top-Down DP (Memoization)")
    print("2. Fibonacci using Bottom-Up DP (Tabulation)")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter value of n: "))
        result = fibonacci_top_down(n)
        print(f"Fibonacci({n}) using Top-Down DP = {result}")

    elif choice == 2:
        n = int(input("Enter value of n: "))
        result = fibonacci_bottom_up(n)
        print(f"Fibonacci({n}) using Bottom-Up DP = {result}")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")