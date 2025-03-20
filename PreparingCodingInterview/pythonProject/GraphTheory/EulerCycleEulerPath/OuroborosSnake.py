from typing import List, DefaultDict
from collections import defaultdict


class TargetEdge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight


class DeBruijnNode:
    def __init__(self, sequence, nid: int):
        self.sequence = sequence
        self.nid = nid


class DeBruijnEdge:
    def __init__(self, u: DeBruijnNode, v: DeBruijnNode, eid: int):
        self.u: DeBruijnNode = u
        self.v: DeBruijnNode = v
        self.sequence: str = self.u.sequence + self.v[-1]
        self.eid = eid


def next_sequence(seq: str) -> str:
    lst_idx = len(seq) - 1

    while lst_idx > 0 and seq[lst_idx] == '1':
        lst_idx -= 1
    if lst_idx == 0 and seq[lst_idx] == '1':
        return seq
    res = seq[:lst_idx] + str(1)
    for i in range(lst_idx + 1, len(seq)):
        res += 0
    return res


class BuildingBinaryDeBruijnGraph:
    def __init__(self, n):
        self.n = n
        self.edges: DefaultDict[str, List[DeBruijnEdge]] = defaultdict(list)
        self.nodes: dict = dict()

    def build(self):
        curr = ''
        for _ in range(self.n):
            curr += '0'
        node = DeBruijnNode(curr, 0)
        self.nodes[curr] = node
        num_node = 2 ** self.n
        counter = 0
        for i in range(num_node):
            curr = next_sequence(curr)
            new_node = DeBruijnNode(curr, i)
            self.nodes[curr] = new_node
            next_0 = self.nodes.get(curr[1:] + '0', None)
            next_1 = self.nodes.get(curr[1:] + '1', None)
            prev_0 = self.nodes.get('0' + curr[:-1], None)
            prev_1 = self.nodes.get('1' + curr[:-1], None)
            if next_0 is not None:
                new_edge = DeBruijnEdge(new_node, next_0, counter)
                self.edges[curr].append(new_edge)
                counter += 1
            if next_1 is not None:
                new_edge = DeBruijnEdge(new_node, next_1, counter)
                self.edges[curr].append(new_edge)
                counter += 1
            if prev_0 is not None:
                new_edge = DeBruijnEdge(prev_0, new_node, counter)
                self.edges['0' + curr[:-1]].append(new_edge)
                counter += 1
            if prev_1 is not None:
                new_edge = DeBruijnEdge(prev_1, new_node, counter)
                self.edges['1' + curr[:-1]].append(new_edge)
                counter += 1


class OuroborosSnakeSolution:
    def __init__(self, n, k):
        self.k = k
        self.n = n
        self.g: BuildingBinaryDeBruijnGraph = BuildingBinaryDeBruijnGraph(self.n - 1)
        self.marks: List[int] = [False for _ in range(2 ** n)]

    def solve(self) -> str:
        self.g.build()
        beg = ''
        for _ in range(self.n - 1):
            beg += '0'
        cycle_edges = self.euler_walk(beg)

        ourboros = cycle_edges.pop(0).sequence

        for e in cycle_edges[:-1]:
            ourboros += e.sequence[-1]

        return ourboros[self.k + 1]

    def euler_walk(self, curr: str) -> List[DeBruijnEdge]:

        res: List[DeBruijnEdge] = []

        seq = curr
        while len(self.g.edges[seq]) != 0:

            self.g.edges[seq].sort(key=lambda e: e.sequence)
            next_edge = self.g.edges[seq].pop(0)

            if self.marks[next_edge.eid]:
                continue
            self.marks[next_edge.eid] = True
            res.append(next_edge)
            seq = next_edge.v.sequence

        clone_res = list(res)

        for i in range(len(clone_res) - 2, -1, -1):
            curr_node = clone_res[i].v

            sub_cycle = self.euler_walk(curr_node.sequence)

            res = res[:i + 1] + sub_cycle + res[i + 1:]
        return res
