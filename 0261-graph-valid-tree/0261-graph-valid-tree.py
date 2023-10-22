from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        if len(edges) < n - 1:
            return False

        graph = {i: [] for i in range(n)}
        degree = [0] * n

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            degree[n1] += 1
            degree[n2] += 1
        
        queue = deque([])
        visited = set()

        for i, d in enumerate(degree): 
            if d == 1:
                queue.append(i)
                visited.add(i)

        while queue:
            node = queue.pop()
            
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if neighbor not in visited and degree[neighbor] == 1:
                    queue.appendleft(neighbor)
                    visited.add(neighbor)
        
        return len(visited) == n