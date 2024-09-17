from typing import Optional, List
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val: int = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        q: List[Node] = []
        q_clone = []

        q.append(node)
        cl_node : Node = Node(node.val, [])
        clone_dic = {}
        q_clone.append(cl_node)
        clone_dic[cl_node.val] = cl_node
        visited: List[bool] = [False for _ in range(101)]
        while len(q) != 0:
            curr = q.pop(0)
            clone_curr = q_clone.pop(0)
            visited[curr.val] = True

            for neigh in curr.neighbors:

                if visited[neigh.val]:
                    neigh_clone = clone_dic[neigh.val]
                    clone_curr.neighbors.append(neigh_clone)
                    continue
                q.append(neigh)
                neigh_clone = Node(neigh.val, [])
                clone_curr.neighbors.append(neigh_clone)
                q_clone.append(neigh_clone)
                clone_dic[neigh_clone.val] = neigh_clone
        return cl_node


node_1 = Node(1, [])
head = node_1
node_3 = Node(3, [])
node_2 = Node(2, [])
node_4 = Node(4, [])

node_1.neighbors.extend([node_2, node_4])

node_2.neighbors.extend([node_1, node_3])
node_3.neighbors.extend([node_2, node_4])
node_4.neighbors.extend([node_1, node_3])

cloned_head = Solution().cloneGraph(head)

print(cloned_head.val)