# Created by Jinwook Lim (Aiden Lim) at 7:11 PM 2021/06/22
__author__ = "Jinwook Lim (Aiden Lim)"

"""
BFS can't implemented by recursive method.
"""


def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if not w in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered


if __name__ == "__main__":
    """
    Graph can be defined "Adjacency List" or "Adjacency Matrix"
    Define graph as a Adjacency List
    """
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3],
    }

    result = iterative_bfs(start_v=1)
    print(result)
