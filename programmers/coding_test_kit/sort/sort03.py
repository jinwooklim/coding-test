def other_solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


def solution(citations):
    citations.sort(reverse=True)
    returns = []
    for i, c in enumerate(citations):
        if c > i:
            returns.append(i)
        else:
            return i

    return max(returns) + 1


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    citations = [22, 42]
    citations = [22]

    res = solution(citations)
    print("res : ", res)
