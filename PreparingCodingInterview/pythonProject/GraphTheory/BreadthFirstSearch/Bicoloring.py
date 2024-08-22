from typing import List
from queue import Queue
white = 0
black = 1

class ColorNode:
    def __init__(self, nid: int, color: int = -1):
        self.nid: int = nid
        self.color: int = color
    def set_color(self, color: int):
        self.color = color
        
    def is_white(self) -> bool:
        return self.color == white

class BicoloringSolution:
    def __init__(self,n: int, m: int, g: List[List[int]]):

        self.n: int = n
        self.m: int = m
        self.g: List[List[int]] = g

    def build_color_graph(self) -> (List[ColorNode], List[List[ColorNode]]):

        color_g: List[List[ColorNode]] = [[] for _ in range(self.n + 1)]
        nodes: List[ColorNode] = [ColorNode(i) for i in range(self.n + 1)]
        for u in range(1, self.n + 1):
            for v in self.g[u]:
                color_g[u].append(nodes[v])

        return nodes, color_g

    def solve_is_bipartite_by_bfs(self) -> bool:

        nodes, color_g = self.build_color_graph()

        visited = [False for _ in range(self.n + 1)]

        q: Queue = Queue(maxsize= self.n)
        nodes[1].set_color(white)
        q.put(nodes[1])
        while not q.empty():

            curr_node = q.get()

            opposite_color = black if curr_node.is_white() else white

            for node_v in color_g[curr_node.nid]:

                if visited[node_v.nid]:
                    if node_v.color != opposite_color:
                        return False
                    continue

                visited[node_v.nid] = True
                node_v.color = opposite_color
                q.put(node_v)

        return True

