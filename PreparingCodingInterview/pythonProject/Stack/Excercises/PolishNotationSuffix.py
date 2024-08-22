from typing import List, Dict
from collections import deque
import re

priority_operator: Dict[str, int] = {'^': 0, "*": 1, '/': 1, '+': 2, '-': 2}


def is_operand(s: str) -> bool:
    pattern = '^[a-zA-Z0-9]*$'

    match = re.match(pattern, s)

    if match:
        return True
    return False


def is_operator(s: str) -> bool:
    operators = '^*/+-'

    return s in operators


def is_open_parenthesis(s: str) -> bool:
    return s in '([{'


def is_close_parenthesis(s: str) -> bool:
    return s in ')]}'


class PolishNotationSuffix:
    def to_polish_expr_suffix(self, normal_expr: str) -> str:

        split_expr: List[str] = []

        cur_buff = ''
        for c in normal_expr:
            if is_operator(c):
                if cur_buff:
                    split_expr.append(cur_buff)
                    cur_buff = ''
                split_expr.append(c)
            elif is_operand(c):
                cur_buff += c
            elif is_open_parenthesis(c):
                split_expr.append(c)
            elif is_close_parenthesis(c):
                if cur_buff:
                    split_expr.append(cur_buff)
                    cur_buff = ''
                split_expr.append(c)

        if cur_buff:
            split_expr.append(cur_buff)

        s: deque = deque()

        suffix_expr = ''

        for o in split_expr:
            if is_operand(o):
                suffix_expr += '|' + o
            elif is_operator(o):
                while s and not is_open_parenthesis(s[-1]) and priority_operator[s[-1]] <= priority_operator[o]:
                    suffix_expr += '|' + s.pop()

                s.append(o)
            elif is_open_parenthesis(o):
                s.append(o)
            elif is_close_parenthesis(o):

                while s and is_operator(s[-1]):
                    suffix_expr += '|' + s.pop()

                if s and is_open_parenthesis(s[-1]):
                    s.pop()

        while s:
            suffix_expr += s.pop()
        return suffix_expr

    def evalRPN(self, tokens: List[str]) -> int:

        s: List[int] = []

        for o in tokens:
            if o not in '+-*/':
                s.append(int(o))
                continue

            operand2, operand1 = s.pop(), s.pop()

            if o == '+':
                s.append(operand1 + operand2)
            elif o == '-':
                s.append(operand1 - operand2)
            elif o == '*':
                s.append(operand1 * operand2)
            elif o == '/':
                s.append(int(operand1 / operand2))

        return s[-1]


sln = PolishNotationSuffix()

normal_expr1 = '(1+2)*777-2^3'

print(sln.to_polish_expr_suffix(normal_expr1))

tokens1 = ["4", "13", "5", "/", "+"]

print(sln.evalRPN(tokens1))
