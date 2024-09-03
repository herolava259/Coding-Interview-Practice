from typing import List


class AsteroidCollisionSolution:
    def __init__(self, asteroids: List[int]):
        self.asteroids: List[int] = asteroids

    def solve(self) -> List[int]:

        st: List[int] = []

        for ast in self.asteroids:

            if not st:
                st.append(ast)
                continue

            destroyed = False
            while st and st[-1] >= 0 >= ast:
                if abs(st[-1]) > abs(ast):
                    destroyed = True
                    break
                elif abs(st[-1]) == abs(ast):
                    destroyed = True
                    st.pop()
                    break
                else:
                    st.pop()
            if not destroyed:
                st.append(ast)

        return st


asteroids1 = [10,2,-5]

sln = AsteroidCollisionSolution(asteroids1)

print(sln.solve())
