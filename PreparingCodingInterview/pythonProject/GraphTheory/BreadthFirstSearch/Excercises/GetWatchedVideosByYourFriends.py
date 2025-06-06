from typing import List, Deque, Tuple
from collections import deque, Counter

class WatchedVideoByFriendsSolution:
    def __init__(self, watched_videos: List[List[str]], friends: List[List[int]], idx: int, level: int):
        self.watched_videos: List[List[str]] = watched_videos
        self.friends: List[List[int]] = friends
        self.idx: int = idx
        self.level: int = level

    def solve(self) -> List[str]:
        n = len(self.friends)
        q: Deque[Tuple[int, int]] = deque()
        visited: List[bool] = [False] * n
        visited[self.idx] = True
        q.append((self.idx, 0))
        k_level_watched_videos: List[str] = []
        shortest_path = [n+1] * n
        shortest_path[self.idx] = 0
        while q:
            u, cur_level = q.popleft()
            if cur_level == self.level+1:
                break
            nxt_level = cur_level + 1
            for v in self.friends[u]:
                if nxt_level <= shortest_path[v]:
                    shortest_path[v] = nxt_level
                    k_level_watched_videos.extend(self.watched_videos[v]) if nxt_level == self.level else None
                if visited[v]:
                    continue
                visited[v] = True

                q.append((v, nxt_level))

        freq_watching = Counter(k_level_watched_videos)
        return list(map(lambda c: c[0], sorted(freq_watching.items(), key=lambda x: (x[1], x[0]))))



if __name__ == '__main__':
    watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
    friends = [[1,2],[0,3],[0,3],[1,2]]
    idx = 0
    level = 2

    print(WatchedVideoByFriendsSolution(watchedVideos, friends, idx, level).solve())






