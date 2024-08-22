from typing import List, Optional
import re


class ExprNode:
    def __init__(self, val: str, left_node: Optional['ExprNode'] = None, right_node: Optional['ExprNode'] = None):
        self.val: str = val
        self.left_node: Optional['ExprNode'] = left_node
        self.right_node: Optional['ExprNode'] = right_node


priority_operators = {'^': 0, '*': 1, '/': 1, '+': 2, '-': 2}


def is_open_parenthesis(s: str):
    return s in '({['


def is_close_parenthesis(s: str):
    return s in ')]}'


def is_number(s: str):
    pattern = '^[0-9]*$'

    matcher = re.match(pattern, s)

    if matcher:
        return True
    else:
        return False


def is_operator(s: str):
    return s in '^*+-'

def is_unary_operator(s: str):
    pattern = '^\@(+|-)$'

    match = re.match(pattern, s)

    if match:
        return True

    return False

class BinaryExpressionTree:

    def __init__(self, s: str):
        self.s: str = s

    def get_polish_suffix_expr(self) -> List[str]:

        normal_expr: List[str] = []

        operands = ''
        for o in self.s:
            if o == '(':
                normal_expr.append(o)
            elif o == ')':
                if operands:
                    normal_expr.append(operands)
                    operands = ''
                normal_expr.append(o)
            elif is_operator(o):
                normal_expr.append(o)
            elif is_number(o):
                operands += o
        if operands:
            normal_expr.append(operands)
        s: List[str] = []

        suffix_expr: List[str] = []

        for idx, o in enumerate(normal_expr):

            if is_open_parenthesis(o):
                s.append(o)
            elif is_number(o):
                suffix_expr.append(o)
            elif is_operator(o):

                while s and is_operator(s[-1]) and priority_operators[s[-1]] >= priority_operators[o]:
                    suffix_expr.append(s.pop())
                if idx == 0 or is_open_parenthesis(normal_expr[idx-1]):
                    s.append(f'@{o}')
                else:
                    s.append(o)
            elif is_close_parenthesis(o):

                while s and is_operator(s[-1]):
                    suffix_expr.append(s.pop())

                if s:
                    s.pop()

        while s:
            o = s.pop()
            if is_operator(o):
                suffix_expr.append(o)

        return suffix_expr

    def build_tree(self) -> ExprNode:

        suffix_expr: List[str] = self.get_polish_suffix_expr()

        st_node: List[ExprNode] = []

        for o in suffix_expr:
            if is_unary_operator(o):
                par_node = ExprNode(o)
                child_node = st_node.pop()
                par_node.left_node = child_node
                st_node.append(par_node)
            elif is_operator(o):

                right_node, left_node = st_node.pop(), st_node.pop()

                par_node = ExprNode(o, left_node, right_node)

                st_node.append(par_node)
            elif is_number(o):
                st_node.append(ExprNode(o))

        return st_node[-1]

