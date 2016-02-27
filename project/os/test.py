#ref: http://networkx.readthedocs.org/en/networkx-1.11/tutorial/index.html

class Graph(object):
    """
    Base class for undirected graphs.

    A graph stores nodes and edges with optional data, or attributes.

    Nodes: ISP, AS, Client

    Edges: ISP <-> AS, AS <-> AS, AS <-> Client
    """

    self.nodes = dict()

    def __init__(self):
        pass

    def get_nodes(self):
        """Return a list of nodes."""
        pass

    def get_edges(self):
        """Return a list of edges."""
        pass

    def get_neighbors(self, node):
        """Return a list of neighbors of the node given."""
        pass

    def add_node(self, node, **attr):
        if node not in self.nodes:
            self.nodes[node] = attr
        else:
            self.nodes[node].update(attr)

    def add_edge(self, u, v, weight=-1):
        # add nodes automatically if they are not already in the graph.
        if u not in self.nodes:
            self.nodes[u] = dict()
        if v not in self.nodes:
            self.nodes[v] = dict()

