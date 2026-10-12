class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = []
        for i in range(n+1):
            parent.append(i)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in edges:
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return [a, b]
                
            parent[rootA] = rootB
        