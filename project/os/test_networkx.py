import networkx as nx

# G = nx.Graph()
# G.add_edge('A', 'B', weight=4)
# G.add_edge('B', 'D', weight=2)
# G.add_edge('A', 'C', weight=3)
# G.add_edge('C', 'D', weight=4)
# print G.nodes()
# print G.edges(data=True)
# print nx.shortest_path(G, 'A', 'D', weight='weight')

G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2,3])

G.add_edge(1,2)
G.add_edges_from([(1,3), (2,3)])

print G.nodes()
print G.number_of_nodes()

print G.edges()
print G.number_of_edges()

print G.neighbors(1)


G.add_node(4, time='5pm')
print G.node[4]
G.node[4]['room'] = 714
print G.nodes()
print G.nodes(data=True)