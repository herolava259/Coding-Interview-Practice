from typing import List, Tuple, Dict


class ShortestPathInGraphResolver(object):
    def __init__(self, weighted_graph: List[List[Tuple[int, int]]]):
        self.wg = weighted_graph


    def __call__(self) -> Dict[int, int]:
        pass


class CountingShortestPathSolution:
    def __init__(self, g: List[List[Tuple[int, int]]], s = 1):
        self.g = g
        self.s = s

    def solve(self) -> List[int]:

        dp = [0] * len(g)

        #TODO: solve problem here
        
        return dp