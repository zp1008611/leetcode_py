"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # 初始化最小长度为无穷大
        min_length = float('inf')
        # 初始化窗口的左右边界和窗口内元素的和
        left, current_sum = 0, 0

        # 右边界从 0 开始向右移动
        for right in range(n):
            # 累加当前元素到窗口内元素的和
            current_sum += nums[right]
            # 当窗口内元素的和大于等于目标值时
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 缩小窗口，减去左边界元素
                current_sum -= nums[left]
                # 左边界右移
                left += 1

        # 如果最小长度仍为无穷大，说明没有找到符合条件的子数组，返回 0
        return min_length if min_length != float('inf') else 0