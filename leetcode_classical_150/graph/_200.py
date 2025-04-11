"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

"""

"""
解题思路
可以使用深度优先搜索（DFS）或广度优先搜索（BFS）来解决此问题。这里以深度优先搜索为例，具体步骤如下：

遍历二维网格，当遇到值为 '1' 的陆地时，开始进行深度优先搜索。
在深度优先搜索过程中，将已访问的陆地标记为 '0'，避免重复访问。
每完成一次深度优先搜索，就意味着找到了一个岛屿，岛屿数量加 1
"""

"""
DFS：找到起点，开始搜索（压入栈），识别是否可用（弹出栈，然后识别），可用就标记，继续搜索邻居（把邻居压入栈）
"""


from typing import List

# DFS的递归形式
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # 检查坐标是否越界、当前位置不是陆地或已访问
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            # 将当前陆地标记为已访问，这里使用 '-1'
            grid[r][c] = '-1'
            # 对当前位置的上下左右进行深度优先搜索
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # 遇到陆地，开始深度优先搜索
                    dfs(r, c)
                    # 完成一次搜索，岛屿数量加 1
                    count += 1

        return count
    
# DFS的栈形式
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    stack = [(r, c)]
                    while stack:
                        # 弹出栈顶元素
                        row, col = stack.pop()
                        # pop方法用于移除列表中指定位置的元素，并返回该元素的值。
                        # 若不指定位置，默认移除并返回列表的最后一个元素。
                        # 检查坐标是否越界、当前位置不是陆地或已访问
                        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                            continue
                        # 将当前陆地标记为已访问，这里使用 '-1'
                        grid[row][col] = '-1'
                        # 将当前位置的上下左右加入栈中
                        stack.extend([(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])
                        # extend方法用于在列表的末尾一次性追加另一个可迭代对象（如列表、元组、字符串等）中的所有元素。
                    # 完成一次搜索，岛屿数量加 1
                    count += 1
        return count

                    
        
        