# Created by Jinwook Lim (Aiden Lim) at 7:05 PM 2021/06/21
__author__ = "Jinwook Lim (Aiden Lim)"

"""
Binary Search
: 정렬되어있는 배열에서 데이터를 찾을 때, 순차 탐색과 달리 탐색 범위를 절반씩 줄여가며 찾아가는 search 방법.
"""


def binary_search(arr, data):
    first = 0
    last = len(arr)
    while first <= last:
        middle = (first + last) // 2
        if arr[middle] == data:
            return middle
        elif arr[middle] > data:
            last = middle - 1
        else:
            first = middle + 1
    return -1


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    target = 5
    idx = binary_search(data, target)
    print(idx)
