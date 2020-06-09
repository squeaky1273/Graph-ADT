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

    # TODO: Use 'open' to open the file
    with open(filename) as f:
        lines = next(f).strip('\n')
        
        if lines == "G":
            graph = Graph(is_directed=False)
        elif lines == "D":
            graph = Graph()
        else:
            raise ValueError('Invalid graph type')

        next_line = next(f).strip('\n').split(',')

        for _ in next_line:
            graph.add_vertex(_)

        for line in f:
            graph.add_edge(line[1], line[3])
            
        return graph


if __name__ == '__main__':

    graph = read_graph_from_file('test.txt')
    print(graph)