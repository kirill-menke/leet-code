from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            
        visited = set()
        counter = 0
        
        for node in range(n):
            if node in visited:
                continue
            
            stack = [node]
            visited.add(node)
            counter += 1
            
            while stack:
                next_node = stack.pop()
                for neigh in graph[next_node]:
                    if neigh not in visited:
                        stack.append(neigh)
                        visited.add(neigh)
        
        return counter
        
        