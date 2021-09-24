def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com
        res = sorted(array[i - 1 : j])[k - 1]
        answer.append(res)

    return answer


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    res = solution(array, commands)
    print("res : ", res)
