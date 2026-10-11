class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        for req in prerequisites:
            graph[req[1]].append(req[0])

        visited = set()
        visiting = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            
            order.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order[::-1]
            


        