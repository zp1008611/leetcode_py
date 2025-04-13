"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

 

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
 

提示：

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

"""
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # 用于标记城市是否被访问过
        visited = [False] * n
        # 省份数量
        provinces = 0

        def dfs(i):
            # 标记当前城市已访问
            visited[i] = True
            for j in range(n):
                # 如果两个城市相连且未被访问过，则进行深度优先搜索
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                # 若城市未被访问过，进行深度优先搜索，并增加省份数量
                dfs(i)
                provinces += 1

        return provinces