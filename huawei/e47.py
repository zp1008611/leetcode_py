"""
题目
在学校中，N 个小朋友站成一队， 第 i 个小朋友的身高为height[i]，第 i 个小朋友可以看到的第一个比自己身高更高的小朋友 j ，那么 j 是 i 的好朋友(要求j > i)。

请输出一个数组，对应位置的输出是每个小朋友的好朋友位置，如果没有看到好朋友，则输出0。

输入描述

第一行输入N，N表示有N个小朋友

第二行输入N个小朋友的身高height[i]，都是整数

输出描述

输出N个小朋友的好朋友的位置

示例1：

输入

2

100 95

输出

0 0

示例2：

输入：

8 123 124 125 121 119 122 126 123

输出：

1 2 6 5 5 6 0 0

"""


def method1(nums):
    # 复制数组
    temp = nums[:]
    for i in range(len(nums)):
        # 初始化每个小朋友的好朋友位置为 0
        temp[i] = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                # 找到好朋友，记录位置并跳出内层循环
                temp[i] = j
                break
    return temp

# 用栈的方法
def method2(nums):
    n = len(nums)
    # 初始化结果数组，初始值都为 0
    result = [0] * n
    # 初始化单调栈
    stack = []

    for i in range(n):
        # 当栈不为空且当前小朋友身高大于栈顶小朋友身高
        while stack and nums[stack[-1]] < nums[i]:
            # 栈顶小朋友的好朋友位置为当前小朋友的位置
            result[stack.pop()] = i
        # 将当前小朋友的索引入栈
        stack.append(i)

    return result

# 读取小朋友的数量，这里原代码未处理该输入，导致逻辑错误
n = int(input())
# 读取小朋友的身高列表
nums = list(map(int, input().split()))
temp = method1(nums)
# 将整数数组转换为字符串数组
str_temp = [str(x) for x in temp]
print(" ".join(str_temp))
