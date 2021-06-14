# Created by Jinwook Lim (Aiden Lim) at 7:30 PM 2021/06/14
__author__ = "Jinwook Lim (Aiden Lim)"


def selection_sort(data: list, ascending=True):
    """
    In the worst case, It has O(N^2).

    1. Compare two element.
    2. If conditioned, change them.

    :param data:
    :return:
    """

    length = len(data)
    for i in range(length):
        min = i

        for j in range(i + 1, length):
            if ascending:
                if data[j] < data[min]:
                    min = j
            else:
                if data[j] > data[min]:
                    min = j

        if min == i:
            continue

        temp = data[i]
        data[i] = data[min]
        data[min] = temp

    return data


if __name__ == "__main__":
    test = []
    test.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    test.append([9, 8, 7, 6, 5, 4, 3, 2, 1])
    test.append([1, 3, 2, 4, 6, 8, 7, 5, 9])
    for data in test:
        result = selection_sort(data)
        print(result)

        result = selection_sort(data, ascending=False)
        print(result)
