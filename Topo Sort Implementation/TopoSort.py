#  File: TopoSort.py

#  Description: Implement the Topological Sort and run it on inputted graphs to output whether or not a Cycle exists and the list of vertices after a sort.

#  Date Created: 11-18-2021

#  Date Last Modified: 11-22-2021

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    def current(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []  # a list of vertex objects
        self.adjMat = []  # adjacency matrix of edges

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (
                    not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # return an adjacent vertex  to vertex v (index)
    def get_adj_vertexes(self, v):
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0):
                verts.append(i)
        return verts

    def get_adj_back_forth_vertex(self, v):
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) or self.adjMat[i][v] > 0:
                verts.append(i)
        return verts

    # do the depth first search in a graph from vertex v (index)
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # cycle check
        cyclic = False

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        # print(self.Vertices[v])
        theStack.push(v)

        # visit the other vertices according to depth
        while (not theStack.is_empty()) and not cyclic:
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            # print(u)
            # print(theStack.__str__())
            adjacents = self.get_adj_vertexes(u)
            # print(adjacents)
            if v in adjacents:
                # print(v)
                final_adjacents = self.get_adj_back_forth_vertex(v)
                # print(final_adjacents)
                # print(u)
                if u in final_adjacents:
                    cyclic = True
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                # print(self.Vertices[u])
                theStack.push(u)
                # if cyclic:
                #     theStack.clear()

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return cyclic
        # determine if a directed graph has a cycle
        # this function should return a boolean and not print the result

    # Checks and returns True or False if there is a Cycle in the graph. Uses Depth First Searching.
    def has_cycle(self):
      # create the Stack
      theStack = Stack()

      # cycle check
      cyclic = False
      for v in range(len(self.Vertices)):

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        # print(self.Vertices[v])
        theStack.push(v)

        # visit the other vertices according to depth
        while (not theStack.is_empty()) and not cyclic:
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            # print(u)
            # print(theStack.__str__())
            adjacents = self.get_adj_vertexes(u)
            # print(adjacents)
            if v in adjacents:
                # print(v)
                final_adjacents = self.get_adj_back_forth_vertex(v)
                # print(final_adjacents)
                # print(u)
                if u in final_adjacents:
                    cyclic = True
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                # print(self.Vertices[u])
                theStack.push(u)
                # if cyclic:
                #     theStack.clear()

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

      return cyclic

    # do the breadth first search in a graph
    def bfs(self, v):
        theQueue = Queue()

        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theQueue.enqueue(v)

        # visit the other vertices according to depth
        while (not theQueue.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theQueue.current())
            if (u == -1):
                u = theQueue.dequeue()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theQueue.enqueue(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        start = self.get_index(fromVertexLabel)
        finish = self.get_index(toVertexLabel)
        if self.adjMat[start][finish] == self.adjMat[finish][start]:
            self.adjMat[start][finish] = 0
            self.adjMat[finish][start] = 0
        else:
            self.adjMat[start][finish] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):
        idx = self.get_index(vertexLabel)
        for row in self.adjMat:
            row.pop(idx)
        self.adjMat.pop(idx)
        self.Vertices.pop(idx)
      

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
      topoList = []
      removeList = []
      vertex_index = 0
      while len(self.Vertices) > 0:
        vertex_index = 0
        while vertex_index < len(self.Vertices):
          visited = False
          vertex = self.Vertices[vertex_index].label
          for i in range (len(self.Vertices)):
            if self.adjMat[i][vertex_index] == 1:
              visited = True
          if visited:
            vertex_index += 1
          else:
            topoList.append(vertex)
            removeList.append(vertex)
            vertex_index += 1
        while len(removeList) > 0:
          self.delete_vertex(removeList[0])
          removeList.pop(0)
      # Complete it!
      return topoList

    # given a label get the index of a vertex
    def get_index2(self, label, VerticesCopy):
        nVert = len(VerticesCopy)
        for i in range(nVert):
            if (label == (VerticesCopy[i]).get_label()):
                return i
        return -1

    def delete_vertex2(self, vertexLabel, adjMatCopy, VerticesCopy):
        idx = self.get_index2(vertexLabel, VerticesCopy)
        # print(self.adjMat[0])
        # print(self.Vertices)
        for row in adjMatCopy:
            row.pop(idx)
        adjMatCopy.pop(idx)
        VerticesCopy.pop(idx)


def main():
    # create a Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices and insert them into the graph
    for i in range(num_vertices):
        line = sys.stdin.readline()
        vertex = line.strip()
        theGraph.add_vertex(vertex)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read the edges and insert them into the graph
    for i in range(num_edges):
        line = sys.stdin.readline()
        line = line.strip()
        edge = line.split()
        #print(edge)
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])
        #print(start, finish)

        theGraph.add_directed_edge(start, finish, 1)

    # print(num_edges)
    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if (not theGraph.has_cycle()):
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)

    
main()
