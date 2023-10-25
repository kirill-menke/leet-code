class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        stack = [(0, -1)]
        visited = set([0])

        while stack:
            node, parent = stack.pop()
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                stack.append((neigh, node))
                visited.add(neigh)
            
        return len(visited) == n