深度优先搜索（DFS）是一种用于遍历或搜索树或图的算法。它沿着树的深度遍历树的节点，尽可能深的搜索树的分支。当节点v的所在边都己被探寻过，搜索将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已发现从源节点可达的所有节点为止。以下为你分别介绍使用递归和迭代方式实现深度优先搜索的方法。

### 递归实现
递归是实现深度优先搜索最直观的方式，它通过不断地递归调用自身来深入探索节点。下面是使用 Python 实现的示例代码：
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start)
        visited.add(start)
        for neighbor in graph[start]:
            dfs_recursive(graph, neighbor, visited)


dfs_recursive(graph, 'A')

```
### 迭代实现
迭代实现通常使用栈来模拟递归调用的过程。以下是使用 Python 实现的示例代码：
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))


dfs_iterative(graph, 'A')

```
### 代码解释
- **递归实现**：`dfs_recursive` 函数接收图、起始节点和一个已访问节点集合作为参数。若起始节点未被访问过，就将其标记为已访问并打印，接着递归地对其所有邻居节点调用 `dfs_recursive` 函数。
- **迭代实现**：`dfs_iterative` 函数使用一个栈来模拟递归调用。先将起始节点压入栈中，然后在栈不为空时，弹出栈顶节点，若该节点未被访问过，就将其标记为已访问并打印，再将其所有邻居节点压入栈中。

通过上述两种方式，你能够实现图的深度优先搜索。递归实现代码简洁，但在处理大规模数据时可能会出现栈溢出问题；迭代实现则使用栈来模拟递归过程，可避免栈溢出问题。 