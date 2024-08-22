from typing import List


class BasicCalculator:
    def __init__(self, s: str):

        self.s = s

    def solve(self) -> int:

        normal_expr: List[str] = []
        operand = ''
        for o in self.s:

            if o == ' ':
                continue
            if o in '()+-':
                if operand:
                    normal_expr.append(operand)
                    operand = ''
                normal_expr.append(o)
            else:
                operand += o

        if operand:
            normal_expr.append(operand)

        suffix_expr = []

        st: List[str] = []

        for idx, o in enumerate(normal_expr):
            if o == '(':
                st.append(o)
            elif o == ')':
                while st and st[-1] != '(':
                    suffix_expr.append(st.pop())
                if st:
                    st.pop()
            elif o in '+-':

                while st and st[-1] != '(':
                    suffix_expr.append(st.pop())

                if idx == 0 or normal_expr[idx-1] in '(+-':
                    st.append('@' + o)
                else:
                    st.append(o)
            else:
                suffix_expr.append(o)

        while st and st[-1] != '(':
            suffix_expr.append(st.pop())

        st: List[int] = []

        for o in suffix_expr:

            if o in '+-':
                oper2, oper1 = st.pop(), st.pop()

                if o == '+':
                    st.append(oper1 + oper2)
                elif o == '-':
                    st.append(oper1 - oper2)
            elif o == '@-':
                st[-1] = -st[-1]
            else:
                st.append(int(o))

        return st[-1]


s1 = '1-(     -2)'
sln1 = BasicCalculator(s1)

print(sln1.solve())
