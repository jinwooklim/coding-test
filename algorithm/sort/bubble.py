# Created by Jinwook Lim (Aiden Lim) at 7:14 PM 2021/06/14
__author__ = "Jinwook Lim (Aiden Lim)"


def bubble_sort(data: list, ascending=True):
    """
    In the worst case, It has O(N^2).

    1. Compare two adjacent element.
    2. If conditioned, change them.

    :param data:
    :param ascending:
    :return:
    """
    length = len(data)
    for i in range(length):
        for j in range(length - 1):
            if ascending:
                if data[i] < data[j]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
            else:
                if data[i] > data[j]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp

    return data


if __name__ == "__main__":
    test = []
    test.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
    test.append([9, 8, 7, 6, 5, 4, 3, 2, 1])
    test.append([1, 3, 2, 4, 6, 8, 7, 5, 9])
    for data in test:
        result = bubble_sort(data)
        print(result)

        result = bubble_sort(data, ascending=False)
        print(result)
