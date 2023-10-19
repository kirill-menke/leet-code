from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming_edges = [0] * numCourses

        for c, pc in prerequisites:
            graph[pc].append(c)
            incoming_edges[c] += 1
        
        result = []
        
        queue = deque([i for i in range(numCourses) if incoming_edges[i] == 0])

        while queue:
            course = queue.pop()
            result.append(course)

            for neigh in graph[course]:
                incoming_edges[neigh] -= 1
                if incoming_edges[neigh] == 0:
                    queue.appendleft(neigh)
        
        return result if len(result) == numCourses else []

                   

