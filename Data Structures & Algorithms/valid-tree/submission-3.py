class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        graph = {}

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        return n > 0 and dfs(0,-1) and len(visited) == n
            


            

        