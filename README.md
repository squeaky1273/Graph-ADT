# Homework 1: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

    Breadth-first Search is different in graphs than in trees because trees have leaves and no cycles. Trees have a strarting point (the root) and go down from there. When using Breadth-first Search in a graph, we have to worry about finding the shortest patha nd not get caught in a never ending loop.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

    One application of Breadth-first Search is a GPS. When using a GPS, the system is looking and nearbly by streets to fing the fastest path to your destinations. When it checks neigboring streets, it then looks at what is beyond there and if there are any potential obstacles that will require more maneuvering.

__________________________________________

1. Compare and contrast Breadth-first Search and Depth-first Search by providing one similarity and one difference.

    One similarity is that both BFS and DFS use the neighbor components when visiting and moving on. One difference is that BFS uses the queues to look for the shortest path and DFS uses Stacks as it's data structure. DFS searches most ro all of the possible paths.

2. Explain why a Depth-first Search traversal does not necessarily find the shortest path between two vertices. What is one such example of a graph where a DFS search would not find the shortest path?

    DFS goes outward to the farthest vertex and makes it's way to unvisited vertices. An example is a maze.

3. Explain why we cannot perform a topological sort on a graph containing a cycle.

    A topological sort is a linear ordering of vertices and return them in order. A graph that has a cycle doesn't end. There is no end point.