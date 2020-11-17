"""
Created on Fri Oct 30 18:43:41 2020

@author: Nik

MITx 6.00.2 Lecture 3 Exercise 2
"""
        
"""
From Lecture 3 Exercise 2 Context
"""

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)


"""
My Answer
"""
g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
#g.addEdge(Edge(nodes[1], nodes[3])) missed the connection between 2 & 3 instead of 1 & 3
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[3], nodes[5]))
g.addEdge(Edge(nodes[4], nodes[5]))
