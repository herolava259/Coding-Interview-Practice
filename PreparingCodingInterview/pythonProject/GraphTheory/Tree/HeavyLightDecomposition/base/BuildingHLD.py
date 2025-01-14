from typing import List, Tuple, Optional
from HLDStructure import GeneralHLDTree


class HLDBuilder:
    def __init__(self, tree: List[List[int]] | None = None, root: int = -1):
        self.root: int = root
        self.tree: List[List[int]] = tree
        self.n: int = len(self.tree)

        #specifications
        self.size: List[int] | None = None
        self.depth: List[int] | None = None
        self.par: List[int] | None = None

        #hld specifications

        self.chain_head: List[int] | None = None
        self.chain_id: List[int] | None = None
        self.pos: List[int] | None = None
        self.arr: List[int] | None = None

    def add_root(self, root: int)-> Optional['HLDBuilder']:

        assert 0 < root < 10**5, 'root should be in exclusive range from 0 to 100000'
        self.root = root
        return self

    def add_tree(self, tree: List[List[int]])->Optional['HLDBuilder']:

        assert tree is not None, 'tree args is not NONE'

        self.tree = tree

        return self


    def init_spec(self) -> Optional['HLDBuilder']:

        size: List[int] = [1] * (self.n+1)
        depth: List[int] = [1] * (self.n+1)
        par: List[int] = [-1] * (self.n+1)

        def dfs_spec(u: int, p: int = -1)->int:
            if p != -1:
                depth[u] = depth[p] + 1
                par[u] = p
            for v in self.tree[u]:
                if v == p:
                    continue
                size[u] += dfs_spec(v, u)

            return size[u]

        self.size, self.depth, self.par = dfs_spec(self.root)

        return self

    def init_hld(self) -> Optional['HLDBuilder']:

        chain_head: List[int] = [0] * (self.n+1)
        chain_id: List[int] = [0] * (self.n+1)
        pos: List[int] = [0] * (self.n+1)
        arr: List[int] = [0] * (self.n+1)

        cur_pos: int = 0
        cur_chain: int = 1

        def hld(u: int, p: int = -1):

            nonlocal cur_pos, cur_chain

            if not chain_head[cur_chain]:
                chain_head[cur_chain] = u

            chain_id[u] = cur_chain
            pos[u] = cur_pos
            arr[cur_pos] = u
            cur_pos += 1
            nxt = 0
            for v in self.tree[u]:
                if v == p:
                    continue

                if not nxt or self.size[v] > self.size[nxt]:
                    nxt = v

            if nxt:
                hld(nxt, u)

            for v in self.tree[u]:
                if v == p or v == nxt:
                    continue

                cur_chain += 1
                hld(v, u)


        hld(self.root)

        self.chain_head, self.chain_id, self.pos, self.arr = chain_head, chain_id, pos, arr

        return self

    def build(self) -> GeneralHLDTree:

        if not self.tree or not self.chain_head or not self.chain_id or not self.pos or not self.arr:
            raise Exception("Cannot build hld properties")

        return GeneralHLDTree(self.root, self.tree, self.chain_head, self.chain_id, self.pos, self.arr,
                                self.par, self.depth)



def init_example() -> GeneralHLDTree:

    tree: List[List[int]] = [[3, 2]]
    root: int = 1
    builder = HLDBuilder(tree, root)

    return builder.init_hld().init_spec().build()


