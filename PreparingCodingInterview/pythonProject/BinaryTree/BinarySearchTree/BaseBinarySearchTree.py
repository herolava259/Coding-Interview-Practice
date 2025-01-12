from typing import List, Optional


class BinarySearchNode:
    def __init__(self, key: int = 0, left_child: Optional['BinarySearchNode'] = None,
                 right_child: Optional['BinarySearchNode'] = None, parent: Optional['BinarySearchNode'] = None,
                 cnt=None):
        self.key: int = key
        self.left_child: BinarySearchNode | None = left_child
        self.right_child: BinarySearchNode | None = right_child
        self.parent: BinarySearchNode | None = parent
        self.cnt = cnt
        self.h:int = 0


class BinarySearchTree:
    def __init__(self, root: Optional['BinarySearchNode'] = None):
        self.root: BinarySearchNode | None = root

    def search(self, key: int) -> BinarySearchNode | None:
        def find_node(cur_node: BinarySearchNode | None, k: int):
            if cur_node is None:
                return None
            if cur_node.key == k:
                return cur_node
            elif cur_node.key < k:
                return find_node(cur_node.right_child, k)
            elif cur_node.key > k:
                return find_node(cur_node.left_child, k)
            return None

        return find_node(self.root, key)

    @staticmethod
    def find_min(root_node: BinarySearchNode):
        def left_most(cur_node: BinarySearchNode | None):
            if not cur_node:
                return None
            if not cur_node.left_child:
                return cur_node
            return left_most(cur_node.left_child)

        return left_most(root_node)

    @staticmethod
    def find_max(root_node: BinarySearchNode):
        def right_most(cur_node: BinarySearchNode | None):
            if not cur_node:
                return None
            if not cur_node.right_child:
                return cur_node
            return right_most(cur_node.right_child)

        return right_most(root_node)

    def minimum(self) -> BinarySearchNode | None:
        return self.find_min(self.root)

    def maximum(self) -> BinarySearchNode | None:

        return self.find_max(self.root)

    def predecessor(self, key: int) -> BinarySearchNode | None:

        root_node = self.search(key)

        if not root_node:
            return None
        if not root_node.left_child:
            return None

        return self.find_max(root_node.left_child)

    def successor(self, key: int) -> BinarySearchNode | None:

        root_node = self.search(key)

        if not root_node:
            return None

        if not root_node.right_child:
            return None
        return self.find_min(root_node.right_child)

    def insert(self, key: int, cnt=None) -> bool:
        def insert_node(newly_node: BinarySearchNode, cur_node: BinarySearchNode) -> bool:
            if newly_node.key == cur_node.key:
                return False
            elif newly_node.key < cur_node.key:
                if not cur_node.left_child:
                    cur_node.left_child = newly_node
                    newly_node.parent = cur_node
                    return True
                else:
                    return insert_node(newly_node, cur_node.left_child)

            if not cur_node.right_child:
                cur_node.right_child = newly_node
                return True
            else:
                return insert_node(newly_node, cur_node.right_child)

        new_node = BinarySearchNode(key, cnt=cnt)

        return insert_node(new_node, self.root)

    def remove(self, key: int) -> bool:
        par_node = self.root
        cur_node = self.root

        while par_node and par_node.key != key:

            left_node = cur_node.left_child
            right_node = cur_node.right_child

            if left_node and left_node.key == key:
                cur_node = left_node
                break
            elif right_node and right_node.key == key:
                cur_node = right_node
                break

            if key < par_node.key:
                cur_node = par_node = left_node
            else:
                cur_node = par_node = right_node

        if not par_node:
            return False
        if par_node.left_child == cur_node:
            par_node.left_child = None
        else:
            par_node.right_child = None

        if not cur_node.left_child and not cur_node.right_child:
            del cur_node
            return True
        replaced_node = self.find_max(cur_node.left_child)

        if not replaced_node:
            if par_node.key > key:
                par_node.left_child = cur_node.right_child
            else:
                par_node.right_child = cur_node.right_child

            if not par_node.right_child:
                par_node.right_child.parent = par_node

            del cur_node
            return True

        par_rl_node = replaced_node.parent

        if par_node != cur_node:
            if par_node.key > key:
                par_node.left_child = replaced_node
            else:
                par_node.right_child = replaced_node
            replaced_node.parent = par_node

        replaced_node.left_child = cur_node.left_child
        replaced_node.right_child = cur_node.right_child

        par_rl_node.right_child = None

        del cur_node
        return True

    def get_sorted_list(self) -> List[int]:

        sorted_arr = []

        def put_element(cur_node: BinarySearchNode, container: List[int]):
            if not cur_node:
                return
            put_element(cur_node.left_child, container)
            container.append(cur_node.key)
            put_element(cur_node.right_child, container)

        put_element(self.root, sorted_arr)

        return sorted_arr

    def print_inorder(self):

        def inorder_print(cur_node: BinarySearchNode | None):
            if cur_node is None:
                return

            inorder_print(cur_node.left_child)
            print(f'key: {cur_node.key}\n content: {cur_node.cnt}\n')
            inorder_print(cur_node.right_child)

        inorder_print(self.root)

    def print_preorder(self):
        def preorder_print(cur_node: BinarySearchNode | None):
            if cur_node is None:
                return

            preorder_print(cur_node.left_child)
            preorder_print(cur_node.right_child)
            print(f'key: {cur_node.key}\n content: {cur_node.cnt}\n')

        preorder_print(self.root)

    def print_postorder(self):
        def postorder_print(cur_node: BinarySearchNode | None):
            if cur_node is None:
                return
            print(f'key: {cur_node.key}\n content: {cur_node.cnt}\n')
            postorder_print(cur_node.left_child)

            postorder_print(cur_node.right_child)

        postorder_print(self.root)
