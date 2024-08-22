from collections import defaultdict
from typing import List


class TopoSortSolution:

    @staticmethod
    def can_finish(numCourses: int, prerequisites: List[List[int]]):

        graph, queue, cnt = defaultdict(list), [], 0
        inDeg = [0] * numCourses

        for j, i in prerequisites:
            graph[i].append(j)
            inDeg[j] += 1
        for i in range(numCourses):
            if inDeg[i] == 0:
                queue.append(i)

        while queue:
            ele = queue.pop(0)
            for j in graph[ele]:
                inDeg[j] -= 1
                if inDeg[j] == 0:
                    queue.append(j)

            cnt += 1
        if cnt == numCourses:
            return True
        else:
            return False
