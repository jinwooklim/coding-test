# Created by Jinwook Lim (Aiden Lim) at 7:01 PM 2021/06/22
__author__ = "Jinwook Lim (Aiden Lim)"


def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


def iterative_dfs(start_v):
    """
    Faster than recursive_dfs
    :param start_v:
    :return:
    """
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

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

    result = recursive_dfs(v=1)
    print(result)
    result2 = iterative_dfs(start_v=1)
    print(result2)
