class Solution(object):
    def calcEquation(self, equations, values, queries):
        g={}
        for (a,b),v in zip(equations,values):
            g.setdefault(a,{})[b]=v
            g.setdefault(b,{})[a]=1.0/v

        # -- Learnings --
        '''
        1. Adjacency list -> the neighbour nodes of the node are taken into Dictionary for the ease. 
        2. DFS -> either Recursion or go for DS stacks/queue/array with pop left basically
        3. This kinda problem can be called as 'Weighted Graph Traversal'
        '''
        def dfs(x,y):
            if x not in g or y not in g:
                return -1.0
            s=[(x,1.0)]
            v=set()
            while s:
                c,r=s.pop()
                if c==y:
                    return r
                v.add(c)
                for n,value in g[c].items():
                    if n not in v:
                        s.append((n,r*value))
            return -1.0 
        return [dfs(x,y) for x,y in queries]
