# Created by Jinwook Lim (Aiden Lim) at 7:01 PM 2021/06/22
__author__ = "Jinwook Lim (Aiden Lim)"


def recursive_dfs(i, discoverd=[]):
    discoverd.append(i)

    for j, value in enumerate(graph[i]):
        if value == 1:
            if not j in discoverd:
                print(i + 1, '->', j + 1)
                recursive_dfs(j, discoverd)

    return discoverd


def iterative_dfs(start_i):
    discovered = []
    stack = [start_i]

    while stack:
        i = stack.pop()
        if i not in discovered:
            discovered.append(i)
            for j, value in enumerate(graph[i]):
                if value == 1:
                    print(i + 1, '->', j + 1)
                    stack.append(j)

    return discovered


if __name__ == "__main__":
    """
    Graph can be defined "Adjacency List" or "Adjacency Matrix"
    Define graph as a Adjacency Matrix
    """
    graph = [
        # 1 2 3 4 5 6 7
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0]
    ]

    result = recursive_dfs(0)
    result = [i + 1 for i in result]  # Just for understanding
    print(result)

    result2 = iterative_dfs(0)
    result2 = [i + 1 for i in result2]  # Just for understanding
    print(result2)
