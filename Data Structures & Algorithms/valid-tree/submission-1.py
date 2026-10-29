class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        edgeMap={i:[] for i in range(n)}

        for u,v in edges:
            edgeMap[u].append(v)
            edgeMap[v].append(u)

        visited=set()

        def dfs(node,parent):
            if node in visited :
                return False

            visited.add(node)

            for neigh in edgeMap[node]:
                if neigh!= parent:
                    if not dfs(neigh,node):
                        return False

            return True
        
        is_tree=dfs(0,-1)

        return is_tree and len(visited)==n
        