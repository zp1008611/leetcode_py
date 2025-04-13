"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List

class Solution:
    pass
def coinChange(coins: List[int], amount: int) -> int:
    # 初始化 dp 数组，dp[i] 表示和为 i 时的最少选取数
    dp = [float('inf')] * (amount + 1)
    # 和为 0 时不需要选取任何数
    dp[0] = 0

    # coins一定在外循环，这样才能得到每个amout-num对应的子问题的答案
    for num in coins:
        for i in range(num, amount + 1):
            # 更新 dp[i] 的值
            # 子问题：寻找amount-num所需最小硬币数
            dp[i] = min(dp[i], dp[i - num] + 1)

    # 如果最终 dp[target] 仍为无穷大，说明无法组成目标和
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
coinChange(coins=coins,amount=amount)