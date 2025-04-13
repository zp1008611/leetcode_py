"""
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

 

示例 1：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1
示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
 

提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）

"""
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 构建图的邻接表
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # 初始化距离数组，用于记录从源节点 k 到各节点的最短距离
        dist = [float('inf')] * (n + 1)
        # 源节点到自身的距离为 0
        dist[k] = 0

        # 优先队列，用于存储 (距离, 节点) 元组，按距离从小到大排序
        pq = [(0, k)]

        while pq:
            # 从优先队列中取出当前距离最小的节点
            current_dist, current_node = heapq.heappop(pq)

            # 如果当前距离大于已记录的最短距离，跳过该节点
            if current_dist > dist[current_node]:
                continue

            # 遍历当前节点的所有邻接节点
            for neighbor, weight in graph[current_node]:
                # 计算从源节点经过当前节点到邻接节点的距离
                distance = current_dist + weight

                # 如果新距离小于已记录的最短距离，更新最短距离并加入优先队列
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        # 找到所有节点中最大的最短距离
        max_delay = max(dist[1:])

        # 如果最大距离为无穷大，说明存在节点无法到达，返回 -1；否则返回最大距离
        return max_delay if max_delay < float('inf') else -1