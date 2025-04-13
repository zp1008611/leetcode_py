"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

 

示例 1：

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。
示例 2：

输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
 

提示：

2 <= cost.length <= 1000
0 <= cost[i] <= 999

"""

from typing import List

# 自底向上
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 获取楼梯的总台阶数
        n = len(cost)
        # 初始化动态规划数组，dp[i] 表示到达第 i 个台阶的最低花费
        dp = [0] * (n + 1)
        # 从第 2 个台阶开始计算，因为可以从第 0 或第 1 个台阶开始
        for i in range(2, n + 1):
            # 状态转移方程，到达第 i 个台阶的最低花费是到达第 i-1 个台阶的最低花费加上第 i-1 个台阶的费用
            # 或者是到达第 i-2 个台阶的最低花费加上第 i-2 个台阶的费用，取两者中的较小值
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
    
# 自顶向下
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(index):
            # 如果索引小于 0，说明不需要花费，返回 0
            if index < 0:
                return 0
            # 如果索引为 0 或 1，返回对应台阶的费用
            if index == 0 or index == 1:
                return cost[index]
            # 递归计算到达当前台阶的最小花费，取从前一个台阶和前两个台阶过来的最小值加上当前台阶的费用
            return cost[index] + min(helper(index - 1), helper(index - 2))
        
        n = len(cost)
        # 从倒数第一个和倒数第二个台阶开始计算，取最小值
        return min(helper(n - 1), helper(n - 2))
