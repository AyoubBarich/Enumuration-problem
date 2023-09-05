import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

elist = [(1, 2), (2, 3), (1, 4), (4, 2)]

G.add_edges_from(elist)

Set = nx.maximal_independent_set(G)

Grandom = nx.complete_graph(5)
nx.random_layout(G)


# nx.draw(G)
# plt.show()

# print(set)


def getLexographicalFirstSet(SetA:list , SetB:list):
    """
    returns the set that is first in lexographical order over the other set
    if the sets are equal it returns  
    """
   
    for i in range(min(len(SetA),len(SetB))):
        if SetA[i]< SetB[i]:
            return SetA
        elif SetB[i] < SetA[i] :
            return SetB
        
    return SetA

def genrateFirstMaxIndependentSet(Graph:nx.Graph):
    n = Graph.order()
    print(n)
    # m = Graph.size()
    # print(m)
    maxSet=[]
    forbiddenVertices = set()
    for i in range(1,n+1):
        curAdjPoint= set([k for k in Graph[i]])
        #   forbiddenVertices = list(set    forbiddenVertices) | set(curAdjPoint))

        if i not in forbiddenVertices:
            maxSet.append(i)
            forbiddenVertices = forbiddenVertices.union(curAdjPoint)
        
    return maxSet

# import ordered_set
# heapq change the default compare function to work with ordered set 
# class to work with ordered sets



        
        
        # if !()
        #     if i not in maxSet:
        #         maxSet.append(i)
    


print(genrateFirstMaxIndependentSet(G))
# A = [5,8,9,3]
# B = [5,8,10,3]

# print(getLexographicalFirstSet(A,B))





