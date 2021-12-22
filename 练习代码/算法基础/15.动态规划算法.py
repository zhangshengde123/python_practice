#

def change(self, amount: int, coins: list[int]) -> int:
    dp = [0 for i in range(amount + 1)]
    dp[0] = 1
    for x in coins:
        for i in range(x, amount + 1):
            dp[i] += dp[i - x]
    return dp[amount]

t = change(27,[2, 5, 7])
print(t)