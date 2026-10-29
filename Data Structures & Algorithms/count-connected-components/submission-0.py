class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        res=0
        visited=set()
        def dfs(node,parent):
            if node in visited:
                return 
            
            visited.add(node)

            for neigh in graph[node]:
                if neigh != parent:
                    dfs(neigh,node)
            graph[node]=[]
        
        for i in range(n):
            if graph[i]:
                dfs(i,-1)
                res+=1
            if i not in visited:
                res+=1

        return res
