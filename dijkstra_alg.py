from __future__ import annotations
import math
from typing import Any

class Vertex:
    item: Any
    neighbours: set[tuple[Vertex, int]]
    def __init__(self, item, neighbours):
        self.item = item
        self.neighbours = neighbours

class Graph:
    vertices: dict
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, item):
        self.vertices[item] = Vertex(item, set())

    def add_edge(self, item1, item2, weight):
        if item1 in self.vertices and item2 in self.vertices:
            v1 = self.vertices[item1]
            v2 = self.vertices[item2]

            # Add v1 and v2 to each other neighbours attribute
            v1.neighbours.add((v2, weight))
            v2.neighbours.add((v1, weight))

    def dijkstra(self, start, end):
        unvisited = list(self.vertices.keys())
        visited = set()

        # Create mapping of vertices to tuple of distances and previous node
        dist = {v: (math.inf, None) for v in unvisited}
        dist[start] = (0, None)

        for _ in range(len(unvisited)):
            # Find current smallest distance from origin vertex
            curr_val = self.dijkstra_min(unvisited, dist)

            # Check if no path exists
            if curr_val is None:
                break

            # Assign to vertex instance
            curr_vertex = self.vertices[curr_val]
            curr_distance = dist[curr_val][0]

            for u in curr_vertex.neighbours:
                ver = u[0]
                ver_d = u[1] + curr_distance

                if ver.item in unvisited:
                    if ver_d < dist[ver.item][0]:
                        dist[ver.item] = (ver_d, curr_val)
            unvisited.remove(curr_val)
            visited.add(curr_val)

        # Check if we reached the 'end' node
        distance = dist[end][0]
        if distance == math.inf:
            return 'No path!'

        # Get path
        path = self.dijkstra_path(start, end, dist)

        return distance, path

    def dijkstra_min(self, unvisited, distances):
        # Find vertex from unvisited with the lowest distance from origin
        smallest = math.inf
        vertex = None
        for v in unvisited:
            if distances[v][0] < smallest:
                vertex = v
                smallest = distances[v][0]
        return vertex

    def dijkstra_path(self, start, end, distances):
        # Return backlog path
        curr = end
        path = [end]
        while curr != start:
            path.insert(0, distances[curr][1])
            curr = distances[curr][1]
        return path
