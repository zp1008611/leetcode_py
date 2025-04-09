"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：

连接：一个单元格与水平或垂直方向上相邻的单元格连接。
区域：连接所有 'O' 的单元格来形成一个区域。
围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
通过 原地 将输入矩阵中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。你不需要返回任何值。

 

示例 1：

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

解释：


在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。

示例 2：

输入：board = [["X"]]

输出：[["X"]]

 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'

"""


"""

可以采用深度优先搜索（DFS）或者广度优先搜索（BFS）的方法，这里使用深度优先搜索来解决此问题。
核心思路是先找出所有不被围绕的区域（即与矩阵边缘相连的 'O' 区域），将这些区域的 'O' 标记为其他字符（例如 '#'），
然后遍历整个矩阵，把剩下的 'O' 替换为 'X'，最后再把标记为 '#' 的字符还原为 'O'
"""


"""
岛屿数量的搜索出发点不限，但是这个问题的出发点是边界处出发开始搜索
"""

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # 检查坐标是否越界或者当前位置不是 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            # 将与边缘相连的 'O' 标记为 '#'
            board[r][c] = '#'
            # 对当前位置的上下左右进行深度优先搜索
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 遍历矩阵的上下边界
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        # 遍历矩阵的左右边界
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        # 遍历整个矩阵，将 'O' 替换为 'X'，将 '#' 还原为 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'