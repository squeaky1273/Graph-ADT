from collections import deque
import random

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        new_vertex = Vertex(vertex_id)
        self.__vertex_dict[vertex_id] = new_vertex
        return new_vertex      

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        self.__vertex_dict[vertex_id1].add_neighbor(self.__vertex_dict[vertex_id2])

        if self.__is_directed is False:
            self.__vertex_dict[vertex_id2].add_neighbor(self.__vertex_dict[vertex_id1])
        
    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(self.get_vertex(start_id))

        while queue:
            current_vertex_obj = queue.popleft()
            current_vertex_id = current_vertex_obj.get_id()

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in seen:
                    seen.add(neighbor.get_id())
                    queue.append(neighbor)

        return # everything has been processed

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # queue of vertices to visit next
        queue = deque() 
        queue.append(self.get_vertex(start_id))

        # while queue is not empty
        while queue:
            current_vertex_obj = queue.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    queue.append(neighbor)
                    # print(vertex_id_to_path)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id]

    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.
        
        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for
        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # data type containing the vertex items
        queue = deque() 
        queue.append((start_id, 0))

        # Take note of vetices that were already visited; don't visit again
        visit = set()
        visit.add(start_id)
        
        # List of vertex items that are `target_distance` away from the start vertex
        vertex_target_list = []

        # While searching through queue
        while queue:
            current_vertex_obj = queue.pop() # vertex obj to visit next

            # Define the neighbors of current vertex item
            vertex_neighbors = self.get_vertex(current_vertex_obj[0]).get_neighbors()

            # If the target distance is the same as the current vertex item, append item to new list
            if current_vertex_obj[1] == target_distance:
                vertex_target_list.append(current_vertex_obj[0])

            # When checking the neighbors of current vertex item
            for neighbor in vertex_neighbors:
                if neighbor.get_id() not in visit:
                    queue.append((neighbor.get_id(), current_vertex_obj[1] + 1))
                    visit.add(neighbor.get_id())

        return vertex_target_list

    def is_bipartite(self):
        """
        Return True if the graph is bipartite, and False otherwise.
        """
        queue = deque()
        visited = {}

        keys = list(self.__vertex_dict.keys())
        current = random.choice(keys)
        color = 0

        queue.append(current)
        visited[current] = color

        while queue:
            current = queue.pop()
    
            color = (color + 1) % 2

            neighbors = self.get_vertex(current).get_neighbors()

            for neighbor in neighbors:
                if neighbor.get_id() not in visited.keys():
                    visited[neighbor.get_id()] = color
                    queue.append(neighbor.get_id())
                else:
                    if visited[current] == visited[neighbor.get_id()]:
                        return False
        return True

    def get_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """
        
        # seen = set()
        # current_vertex_id = random.choice(list(self.__vertex_dict.keys()))
        # neighbors = self.get_vertex(current_vertex_id).get_neighbors()
        
        # def component(node):
        #     nodes = set([node])
        #     while nodes:
        #         node = nodes.pop()
        #         seen.add(node)
                
        # for node in neighbors:
        #     if node not in seen:
        #         yield component(node)

        visited = [] 
        connected_components = [] 
        queue = deque()

        keys = list(self.__vertex_dict.keys())
        current = random.choice(keys)
        visited.append(current)
        queue.append(current)

        while queue:
            current = queue.pop()
            connected_components.append(current)

            neighbors = self.get_vertex(current).get_neighbors()

            for neighbor in neighbors:
                if neighbor.get_id() not in visited:
                    visited.append(neighbor.get_id())
                    connected_components.append(neighbor.get_id())

            if len(visited) == len(keys):
                return connected_components
            
            not_visited = [vertex for vertex in keys if vertex not in visited]

            current = random.choice(not_visited)

            visited.append(current)
            queue.append(current)

        return connected_components

        # for _ in range(current_vertex_id): 
        #     visited.append(False) 
        # for v in range(current_vertex_id): 
        #     if visited[v] == False: 
        #         connected_components.append(current_vertex_id) 
        # return connected_components 

    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """
        # stack = set()
        # stack = stack + [start_id]
        # while stack:
        #     current = stack.pop
        #     neighbors = self.get_vertex(current).get_neighbors()
        #     if start_id == target_id:
        #         break

        #     if not self.__vertex_dict.keys(start_id):
        #         return
            
        #     for neighbor in neighbors(start_id):
        #         if neighbor not in stack:
        #             for new_path in self.__vertex_dict.keys():
        #                 if new_path:
        #                     yield new_path

        visited = {start_id: [start_id]}  
  
        # Create a stack for DFS  
        stack = set()
        stack.add(self.get_vertex(start_id)) 
  
        while stack:  
            current_vertex_obj = stack.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()
  
            neighbors = current_vertex_obj.get_neighbors()
            if current_vertex_id == target_id:
                break

            for neighbor in neighbors:  
                if neighbor.get_id not in visited:  
                    stack.add(neighbor) 
                    
                    current_path = visited[current_vertex_id]
                    new_path = current_path + [neighbor.get_id()]
                    visited[neighbor.get_id()] = new_path

        return visited[target_id]


    def dfs_traversal(self, start_id):
        """Visit each vertex, starting with start_id, in DFS order."""

        visited = set() # set of vertices we've visited so far

        def dfs_traversal_recursive(start_vertex):
            print(f'Visiting vertex {start_vertex.get_id()}')

            # recurse for each vertex in neighbors
            for neighbor in start_vertex.get_neighbors():
                if neighbor.get_id() not in visited:
                    visited.add(neighbor.get_id())
                    dfs_traversal_recursive(neighbor)
            return

        visited.add(start_id)
        start_vertex = self.get_vertex(start_id)
        dfs_traversal_recursive(start_vertex)

    def cycleHelper(self, vertex, visited, stack): 
        
        cycle = False
        visited.add(vertex)
        stack.append(vertex)
        neighbors = vertex.get_neighbors()

        for neighbor in neighbors: 
            if neighbor not in visited: 
                cycle = self.cycleHelper(neighbor, visited, stack)
            elif neighbor in stack: 
                return True

        stack.remove(vertex)
  
        if cycle == True:
            return True
  
    def contains_cycle(self): 
        visited = set()
        values = self.__vertex_dict.values()
        stack = []
        for vertex in values: 
            if vertex in visited:
                return False
            else:
                if self.cycleHelper(vertex, visited, stack) == True: 
                    return True
        return False

    def topological_helper(self, vertex, visited, stack): 
  
        # Mark the current node as visited. 
        visited.add(vertex)
        neighbors = vertex.get_neighbors()
  
        # Recur for all the vertices adjacent to this vertex 
        for neighbor in neighbors: 
            if neighbor not in visited: 
                self.topological_helper(neighbor,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.append(vertex)
        return stack
  
    def topological_sort(self):
        """
        Return a valid ordering of vertices in a directed acyclic graph.
        If the graph contains a cycle, throw a ValueError.
        """
        # TODO: Create a stack to hold the vertex ordering.
        # TODO: For each unvisited vertex, execute a DFS from that vertex.
        # TODO: On the way back up the recursion tree (that is, after visiting a 
        # vertex's neighbors), add the vertex to the stack.
        # TODO: Reverse the contents of the stack and return it as a valid ordering. 
        # Mark all the vertices as not visited 

        visited = set()
        stack = []
        values = self.__vertex_dict.values()
  
        for vertex in values: 
            if vertex not in visited: 
                self.topological_helper(vertex, visited, stack) == True 
  
        solution = list()
        for _ in range(len(self.__vertex_dict)):
            solution.append(stack.pop().get_id())
        return solution

