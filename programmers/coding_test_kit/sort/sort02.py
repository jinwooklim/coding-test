def good_solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))


def solution(numbers):
    biglen = 3

    # Deal '12' vs '121' -> '121212' vs '121121121'
    #
    nums = []
    for i, n in enumerate(numbers):
        nums.append((i, str(n) * (biglen)))
    nums.sort(reverse=True, key=lambda tup: tup[1])
    print(nums)

    answer = ""
    for i, _ in nums:
        answer += str(numbers[i])

    # Deal '0000' -> '0'
    return str(int(answer))


if __name__ == "__main__":
    # numbers = [6, 10, 2]
    # numbers = [3, 30, 34, 5, 9]
    numbers = [1, 1, 1, 1]

    res = solution(numbers)
    print("res : ", res)
