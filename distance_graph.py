# vertex classed used to create vertex objects to place inside graph
class Vertex:
    def __init__(self, vertex_id, name, address, city, state, zip_code):
        self.id = vertex_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code


# graph class used to create a graph object which contains vertex objects and weighted edges between vertices
class Graph:
    vertices = []
    edges = []

    # O(N) - takes vertex object, adds it to 2d matrix, and appends all edge weights to zero to fill graph
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        for row in self.edges:
            row.append(0)
        self.edges.append([0] * (len(self.edges) + 1))

    # O(1) - takes two vertex ID's and the weight (distance between the vertices) ads the weight to the intersect
    def add_edge(self, u, v, weight):
        self.edges[u - 1][v - 1] = weight
        self.edges[v - 1][u - 1] = weight

    # O(1) - takes two vertex id's and returns the weight (distance) between them
    def get_distance(self, current_index, package_index):
        return float(self.edges[current_index - 1][package_index - 1])
