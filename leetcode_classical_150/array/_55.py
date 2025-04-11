"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

"""
可以使用贪心算法来解决这个问题，具体思路是：在遍历数组的过程中，记录当前能够到达的最远位置。
如果在遍历结束之前，最远位置能够到达数组的最后一个元素，那么就可以到达最后一个下标。
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 初始化最远可到达位置为 0
        max_reach = 0
        for i in range(len(nums)):
            # 如果当前位置超过了最远可到达位置，说明无法到达当前位置，返回 False
            if i > max_reach:
                return False
            # 更新最远可到达位置
            max_reach = max(max_reach, i + nums[i])
            # 如果最远可到达位置已经超过或等于数组的最后一个下标，返回 True
            if max_reach >= len(nums) - 1:
                return True
        return False
            