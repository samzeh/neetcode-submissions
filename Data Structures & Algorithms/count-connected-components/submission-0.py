class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])

            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])

        visited = set()
        components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components
