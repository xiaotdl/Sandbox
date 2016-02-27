#ref: http://networkx.readthedocs.org/en/networkx-1.11/tutorial/index.html
import random
# random.uniform(1, 10)                # Random float x, 1.0 <= x < 10.0
# random.randrange(1, 10)                 # Integer from 1 to 10
# random.choice('abcdefghij')          # Single random element


class Graph():
    """
    Base class for undirected graphs.

    A graph stores nodes and edges with optional data, or attributes.

    Nodes: ISP, AS

    Edges: ISP <-> AS, AS <-> AS
    """


    def __init__(self):
        self.nodes = []
        self.edges = []

    def get_nodes(self):
        """Return a list of nodes(Node object)."""
        return self.nodes

    def get_edges(self):
        """Return a list of edges(a tuple of from_node, to_node, weight)."""
        return self.edges

    def get_neighbors(self, node):
        """Return a list of neighbors of the node given."""
        neighbors = []
        for edge in self.edges:
            if node == edge[0]:
                neighbors.append((edge[1], edge[2]))
            if node == edge[1]:
                neighbors.append((edge[0], edge[2]))
        return neighbors

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, u, v, weight=-1):
        if u not in self.nodes or v not in self.nodes:
            raise Exception('unknown node found!')
        self.edges.append((u, v, weight))

    def show_graph(self):
        print "all nodes: %s" % self.nodes
        print "all edges: %s" % self.edges
        for node in self.nodes:
            print "node %s has neighbors: %s" % (node, self.get_neighbors(node))


class ISP():
    def __init__(self):
        self.all_files = dict() # a dict of fileid: file_info

    def __repr__(self):
        return 'isp'


class AS():
    def __init__(self, id):
        self.id = id
        self.cache_size = -1
        self.cached_files = dict() # a dict of filename: file_info
        self.clients = []

    def __repr__(self):
        return 'as' + str(self.id)


class Client():
    def __init__(self, id, belong_to_as):
        self.id = id
        self.belong_to_as = belong_to_as

    def __repr__(self):
        return str(self.id)


class File():
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size

    def __repr__(self):
        return "<%s, %s, %s>" % (str(self.id, self.name), str(self.size))

def manual_create():
    print '-'*50
    print '== manual_create =='
    # nodes init
    isp = ISP()
    as1 = AS(1)
    as2 = AS(2)
    as3 = AS(3)

    # graph init
    G = Graph()

    # add nodes
    G.add_node(isp)
    G.add_node(as1)
    G.add_node(as2)
    G.add_node(as3)

    # add edges
    G.add_edge(as1, isp, 1)
    G.add_edge(as2, isp, 1)
    G.add_edge(as3, isp, 1)
    G.add_edge(as1, as2, 0.5)

    # show result
    G.show_graph()

def auto_create():
    print '-'*50
    print '== auto_create =='
    # nodes init
    isp = ISP()
    as_list = []
    nodes_num = random.randrange(5, 10)
    for i in range(1, nodes_num + 1):
        as_list.append(AS(i))

    # graph init
    G = Graph()

    # add nodes
    G.add_node(isp)
    for curr_as in as_list:
        G.add_node(curr_as)

    # add edges
    for curr_as in as_list:
        G.add_edge(curr_as, isp, random.randint(50, 100))

        other_as = list(set(as_list) - set([curr_as]))
        potential_neighbor_as = random.choice(other_as)
        if abs(curr_as.id + nodes_num - potential_neighbor_as.id) % nodes_num < 2:
            for edge in G.get_edges():
                if potential_neighbor_as == edge[0] and curr_as == edge[1]:
                    break # edge already exists
            G.add_edge(curr_as, potential_neighbor_as, random.randint(1, 10))

    # show result
    G.show_graph()

if __name__ == '__main__':
    manual_create()
    auto_create()
