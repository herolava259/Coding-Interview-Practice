from typing import List


class GeneralHLDTree:
    root: int
    tree: List[List[int]]
    chain_head: List[int]
    chain_id: List[int]
    pos: List[int]
    inverse_pos: List[int]
    par: List[int]
    depth: List[int]

    def __init__(self,root: int,  tree: List[List[int]], chain_head: List[int], chain_id: List[int],
                 pos: List[int], inverse_pos: List[int], par: List[int], depth: List[int]):
        self.tree = tree
        self.chain_head = chain_head
        self.chain_id = chain_id
        self.pos = pos
        self.inverse_pos = inverse_pos
        self.root = root

        self.par: List[int] = par
        self.depth: List[int] = depth
