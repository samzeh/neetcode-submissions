class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {}
        visited = set()
        visiting = set()

        for req in prerequisites:
            if req[1] in graph:
                graph[req[1]].append(req[0])
            else:
                graph[req[1]] = [req[0]]
        
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for neighbour in graph.get(course,[]):
                if not dfs(neighbour):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


        

        