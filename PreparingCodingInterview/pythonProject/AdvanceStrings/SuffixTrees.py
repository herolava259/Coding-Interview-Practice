import math
from typing import List

guard_character = "@"


class Node:
    def __init__(self, val: str, parent_node=None, isLeaf: bool = False, child_node_dict: dict = None, idx=0):
        self.chain = val
        self.isLeaf = isLeaf
        self.child_nodes = []
        self.child_node_dict = {}

        if child_node_dict is not None:
            self.child_node_dict = child_node_dict
            self.child_nodes = list(child_node_dict.values())
        self.parent_node = parent_node
        self.idx = idx
        if not self.isLeaf:
            self.child_nodes.append(Node('@', self, isLeaf=True))

    def is_prefix_of(self, other_chain: str):
        return other_chain.find(self.chain) == 0

    def is_root(self):
        return self.chain == ''

    def search_node(self, next_character: str) -> tuple:
        if self.isLeaf:
            return next_character == guard_character, Node(guard_character, isLeaf=True)

        result = (False, None)

        for child in self.child_nodes:
            if child.chain.endswith(next_character):
                result = (True, child)

        return result

    def clone(self, parent_node):
        return Node(self.chain, self.parent_node, self.isLeaf, child_node_dict=dict(self.child_node_dict))

    def end_of_chain(self) -> bool:

        for child in self.child_nodes:
            if child.isLeaf:
                return True

        return False

    def get_depth(self):

        return len(self.chain) + 1


class SuffixNode(Node):
    def __init__(self, idx, val: str, parent_node=None, isLeaf: bool = False, child_node_dict: dict = None):
        super().__init__(val, parent_node, isLeaf, child_node_dict)
        self.sign = val[0]
        self.order = idx

    def full_chain(self):
        if self.isLeaf:
            return self.chain
        return self.chain + guard_character


class Edge:
    def __init__(self, u: Node, v: Node, val=None):

        if len(u.chain) > len(v.chain):
            u, v = v, u
        self.u = u
        self.v = v
        if val is None:
            self.character = self.v.chain[-2] if self.v.isLeaf else self.v.chain[-1]
        else:
            self.character = val


class SuffixTreeUtil:
    @staticmethod
    def should_merge_with_node(node: Node) -> bool:
        return len(node.child_nodes) <= 1

    @staticmethod
    def create_merged_node(node: Node) -> Node | None:
        if SuffixTreeUtil.should_merge_with_node(node):
            return None
        elif node.isLeaf:
            return node

        child_nodes_dict = {}
        for child in node.child_nodes:
            if len(child.child_nodes) == 1:
                new_chain, new_node = SuffixTreeUtil.reduce_node(child)
                new_node = SuffixTreeUtil.create_merged_node(new_node)
                child_nodes_dict[new_chain + new_chain[-1]] = new_node

            else:
                new_node = SuffixTreeUtil.create_merged_node(node)
                child_nodes_dict[new_node.chain[-1]] = new_node

        result = Node(node.chain, node.parent_node, node.isLeaf, child_nodes_dict)

        return result

    @staticmethod
    def reduce_node(node: Node) -> tuple:
        chain = ''
        curr_node = node
        while len(curr_node.child_nodes) == 1:
            chain += node.chain[-1]
            curr_node = node.child_nodes[0]

        return chain, curr_node


class RawSuffixTrie:

    def __init__(self, str_arr: List[str]):

        self.string_chains = str_arr.sort()

        self.tree = []

        self.root_node = Node('', isLeaf=False)

    def build(self):

        for chain in self.string_chains:
            edges = self.create_node(self.root_node, chain)
            self.tree.extend(edges)

    def contain_chain(self, chain: str) -> bool:
        if chain == '':
            return True
        if len(self.root_node.child_nodes) == 0 or self.root_node.isLeaf:
            return False
        curr_node = self.root_node

        for i in range(len(chain)):

            next_node = curr_node.child_node_dict.get(chain[i], None)

            if next_node is None:
                return False

            curr_node = next_node

        return True

    @staticmethod
    def create_node(root_node: Node, chain: str) -> List[Edge]:

        curr_node = root_node
        curr_idx = 0
        while curr_idx < len(chain):
            check, next_node = curr_node.search_node(chain[curr_idx])

            if check:
                curr_node = next_node
            else:
                break
            curr_idx += 1
        result = []
        for i in range(curr_idx, len(chain)):
            new_node = Node(chain[0: i + 1], curr_node, isLeaf=False)
            curr_node.child_nodes.append(new_node)
            curr_node.child_node_dict[chain[i]] = new_node
            result.append(Edge(curr_node, new_node, chain[i]))
            curr_node = new_node

        # create guard node
        if not curr_node.end_of_chain():
            curr_node.child_nodes.append(Node(chain + guard_character, isLeaf=True))
        return result


class EnhancedSuffixTrie:

    def __init__(self, chains: List[str]):
        self.suffix_arr = chains.sort()
        self.root_node = Node('', isLeaf=False)
        self.edges = []

    def build(self):
        for chain in self.suffix_arr:
            if len(chain) == 1:
                new_node = Node(chain, parent_node=self.root_node, isLeaf=False)
                self.root_node.child_nodes.append(new_node)
                new_edge = Edge(self.root_node, new_node, chain)
                self.edges.append(new_edge)
            else:
                new_edges = EnhancedSuffixTrie.create_node(self.root_node, chain)
                if type(new_edges) is list:
                    self.edges.extend(new_edges)
                elif type(new_edges) is Edge:
                    self.edges.append(new_edges)

    def search_node(self, chain: str) -> Node | None:

        exist, node = EnhancedSuffixTrie.search_node_recursive(self.root_node, chain)

        if not exist:
            return None
        return node

    @staticmethod
    def search_node_recursive(curr_node: Node, chain: str) -> (bool, Node | None):
        if curr_node.isLeaf:
            return False, None

        if len(curr_node.child_nodes) == 1:
            if chain.index(curr_node.chain) == 0:
                return True, curr_node
            else:
                return False, None

        if curr_node.chain == chain:
            return True, curr_node
        n = len(curr_node.child_nodes)
        idx = 0
        while idx < n:
            child = curr_node.child_nodes[idx]
            if chain.index(child.chain) == 0:
                break

        if idx == n:
            return False, None

        return EnhancedSuffixTrie.search_node_recursive(curr_node.child_nodes[idx], chain)

    @staticmethod
    def create_node(parent_node: Node, chain: str) -> List[Edge] | Edge | None:

        nxt_par_node = None

        if parent_node.isLeaf:
            return None
        if chain.index(parent_node.chain) == 1 and len(parent_node.child_nodes) == 1:
            new_node = Node(chain, parent_node, isLeaf=False)
            parent_node.child_nodes.append(new_node)
            parent_node.child_node_dict[chain] = new_node
            return Edge(parent_node, new_node, chain[len(parent_node.chain):])

        if len(parent_node.child_nodes) == 1:
            common = EnhancedSuffixTrie.chain_common(chain, parent_node.chain)

            common_node = Node(common, parent_node, isLeaf=False)
            parent_node.child_nodes.append(common_node)
            parent_node.child_node_dict[common] = common_node

            new_node = Node(chain, common_node, isLeaf=False)
            common_node.child_nodes.append(new_node)
            common_node.child_node_dict[chain] = new_node

            return [Edge(parent_node, common_node, chain[len(parent_node.chain)]),
                    Edge(common_node, new_node, chain[len(common_node.chain):])]

        new_parent_node: Node | None = None

        for child in parent_node.child_nodes:
            if not child.isLeaf and EnhancedSuffixTrie.has_common_prefix(chain, child):
                new_parent_node = child
                break

        if new_parent_node is None:
            return None
        return EnhancedSuffixTrie.create_node(new_parent_node, chain)

    @staticmethod
    def has_common_prefix(chain: str, node: Node):

        return chain[0] == node.chain[0]

    @staticmethod
    def chain_common(chain: str, other_chain: str) -> str:

        length_common = 0
        limit_split = min(len(chain), len(other_chain))

        while length_common == limit_split:
            if chain[length_common] != other_chain[length_common]:
                break
            length_common += 1
        return chain[0: length_common]


class Suffix:
    def __init__(self, first_character: str, idx: int, chain: str, order: int = -1):
        self.sign = first_character
        self.id = idx
        self.suffix_chain = chain[idx:]
        self.order = order
        self.primary_key = -1
        self.secondary_key = -1


class SortSuffixOfChainSolution:
    def __init__(self, chain: str):

        self.chain = chain
        full_chain = chain
        self.suffixes = []
        self.suffix_map = []
        self.n = len(chain)
        self.suffix_dict = {}
        for i in range(self.n - 1, -1, -1):
            suffix = Suffix(full_chain[i], i, full_chain[i:])
            self.suffixes.append(suffix)
            self.suffix_dict[i] = suffix

    def start(self):
        self.suffixes.sort(key=lambda c: c.sign)

        curr_key = 0
        curr_character = "@"
        for s in self.suffixes:
            if curr_character != s.sign:
                curr_character = s.sign
                curr_key += 1
            s.primary_key = curr_key

    def set_secondary_key(self, k: int):

        for key in self.suffix_dict.keys():
            secondary_idx = (key + k) % self.n

            self.suffix_dict[key].secondary_key = self.suffix_dict[secondary_idx].primary_key

    def reset_primary_key(self):

        curr_key = 0
        self.suffixes[0].primary_key = 0
        for i in range(1, self.n):
            prev = self.suffixes[i - 1]
            curr = self.suffixes[i]
            if prev.primary_key < curr.primary_key:
                curr_key += 1
            elif prev.primary_key == curr.primary_key and prev.secondary_key < curr.secondary_key:
                curr_key += 1
            curr.primary_key = curr_key

    def group_by_primary_key_and_sort_by_secondary_key(self) -> List[Suffix]:
        result: List[Suffix] = []

        key = self.suffixes[0].primary_key

        bucket = []
        for suffix in self.suffixes:
            if suffix.primary_key == key:
                bucket.append(suffix)
            else:
                bucket.sort(key=lambda x: x.secondary_key)
                result.extend(bucket)
                key = suffix.primary_key
        return result

    def sort(self):
        self.suffixes = self.group_by_primary_key_and_sort_by_secondary_key()

    def solve(self):
        k = 1
        self.start()
        while math.pow(k, 2) <= self.n:
            self.set_secondary_key(k)
            self.sort()
            self.reset_primary_key()
            k += 1

        for idx, suffix in enumerate(self.suffixes):
            self.suffix_map.append(suffix.id)
            suffix.order = idx


class CreateLongestCommonChainOfSuffixTriesSolution:

    def __init__(self, chain: str):
        self.chain = chain
        self.suffix_sort_solution: SortSuffixOfChainSolution = SortSuffixOfChainSolution(chain)
        self.length_common = [0 for _ in range(len(chain) + 1)]
        self.suffix_ranks: List[int] = [0 for _ in range(len(chain) + 1)]
        self.suffix_map: List[int] = []

    def start(self):
        self.suffix_sort_solution.solve()
        self.suffix_map = self.suffix_sort_solution.suffix_map

        for order, idx in enumerate(self.suffix_map):
            self.suffix_ranks[idx] = order

    def solve(self) -> (List[int], List[int]):

        self.start()
        q = 0
        for idx_i in range(len(self.chain)):
            idx_j = self.suffix_map[self.suffix_ranks[idx_i] - 1]

            # find common chain of suffixes[i] and suffixes[i-1] in sorted alphabet suffixes
            # with i = order in sorted suffix idx_i
            while self.chain[idx_i + q] == self.chain[idx_j + q]:
                q += 1
            self.length_common[self.suffix_ranks[idx_i]] = q
            q = max(q - 1, 0)

        return self.suffix_map, self.length_common


class BuildSuffixTries:
    def __init__(self, chain: str):
        chain += guard_character
        self.chain = chain
        self.util = CreateLongestCommonChainOfSuffixTriesSolution(chain)
        self.root_node = Node("", None, isLeaf=False)
        self.suffix_map: List[int] = []
        self.lcs: List[int] = []
        self.edges: List[Edge] = []
        self.leaf_node = Node(guard_character, self.root_node, isLeaf=True)
        BuildSuffixTries.bind_par_child_node(self.root_node, self.leaf_node)

    def start(self):
        self.suffix_map, self.lcs = self.util.solve()

    def solve(self) -> tuple[Node, List[Edge]]:
        self.start()

        x = self.leaf_node

        for idx, suff in enumerate(self.suffix_map[1:]):

            par_node = x
            new_node = Node(self.chain[suff:], par_node, isLeaf=False)
            l_i = self.lcs[idx + 1]
            while len(par_node.chain) > l_i:
                par_node = par_node.parent_node

            if len(par_node.chain) < l_i:
                tmp_node = Node(self.chain[suff:suff + l_i], par_node, isLeaf=False)
                self.edges.append(BuildSuffixTries.bind_par_child_node(par_node, tmp_node))
                par_node = tmp_node

            self.edges.append(BuildSuffixTries.bind_par_child_node(par_node, new_node))

            x = new_node
        return self.root_node, self.edges

    @staticmethod
    def bind_par_child_node(par: Node, child: Node):

        par.child_nodes.append(child)
        child.parent_node = par
        par.child_node_dict[child.chain] = child

        return Edge(par, child, val=child[child.chain.index(par.chain):])


def longest_common_prefix(chain1: str, chain2: str) -> str:
    result = ''
    for i in range(min(len(chain1), len(chain2))):
        if chain1[i] == chain2[i]:
            result += chain1[i]
        else:
            break

    return result


def create_raw_suffix_trie_for_chain(chain) -> RawSuffixTrie:
    suffixes = []

    for idx in range(len(chain) - 1, -1, -1):
        suffixes.append(chain[idx:])

    result = RawSuffixTrie(suffixes)

    result.build()
    return result


def create_merged_suffix_trie_for_chain(chain: str) -> EnhancedSuffixTrie:
    suffixes = []

    for idx in range(len(chain) - 1, -1, -1):
        suffixes.append(chain[idx:])

    result = EnhancedSuffixTrie(suffixes)

    result.build()

    return result
