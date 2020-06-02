from graphs.graph import Graph


def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    graph = None

    with open(filename, "r") as file:
        lines = [line for line in file]

        # Handle first line
        graph_type = lines[0].strip()
        if graph_type == 'D':
            graph = Graph(is_directed=True)
        elif graph_type == 'G':
            graph = Graph(is_directed=False)
        else:
            raise ValueError('Graph type not properly specified')

        # Add vertices
        vertex_ids = lines[1].strip('\n ').split(',')
        for vertex_id in vertex_ids:
            graph.add_vertex(vertex_id)

        # Add edges
        for line in lines[2:]:
            [vertex_id1, vertex_id2] = line.strip('()\n ').split(',')
            graph.add_edge(vertex_id1, vertex_id2)

    return graph

if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')

    print(graph)