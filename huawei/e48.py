"""
题目描述
给你一个整数数组nums，请计算数组的中心位置。数组的中心位置是数组的一个下标， 其左侧所有元素相乘的积等于右侧所有元素相乘的积。
数组第一个元素的左侧积为1，最后一个元素的右侧积为1。 如果数组有多个中心位置，应该返回最靠近左边的那一个，如果数组不存在中心位置，返回-1。

输入

2 5 3 6 5 6

输出

3

"""

def find_center_position(nums):
    # 计算数组所有元素的总乘积
    total_product = 1
    for num in nums:
        total_product *= num

    # 初始化左侧元素的乘积
    left_product = 1
    for i, num in enumerate(nums):
        # 计算右侧元素的乘积
        right_product = total_product // (left_product * num) if num != 0 else 0
        # 判断左侧元素乘积是否等于右侧元素乘积
        if left_product == right_product:
            return i
        # 更新左侧元素的乘积
        left_product *= num
    return -1

# 读取输入
nums = list(map(int, input().split()))
# 调用函数并输出结果
print(find_center_position(nums))