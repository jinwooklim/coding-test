# Created by Jinwook Lim (Aiden Lim) at 7:24 PM 2021/06/15
__author__ = "Jinwook Lim (Aiden Lim)"

import collections


class Hash:
    def put(self, key, value):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError


class ChainingHash(Hash):
    def __init__(self, size=1000):
        super().__init__()
        self.size = size
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # Use modulo hashing
        index = self.hash_function(key)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        else:
            p = self.table[index]
            while p:
                if p.key == key:  # Update the existed value.
                    p.value = value
                    return
                if p.next is None:  # Do nothing, and break the loop
                    break
                p = p.next
            p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        if self.table[index].value is None:
            return -1
        else:
            p = self.table[index]
            while p:
                if p.key == key:
                    return p.value
                p = p.next
            return - 1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        if self.table[index].value is None:
            return
        else:
            # Node is the first in index
            p = self.table[index]
            while p:
                if p.key == key:
                    self.table[index] = ListNode() if p.next is None else p.next
                    return

            # Remove linked node
            prev = p
            while p:
                if p.key == key:
                    prev.next = p.next
                    return
                prev, p = p, p.next

    def hash_function(self, key):
        """
        Use modulo hashing.
        """

        return key % self.size


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class OpenaddressHash(Hash):
    """
    Implement of Open-Address Hashing (Close Hashing or Linear Probing)
    """

    def __init__(self, size=1000):
        self.size = size
        self.table = [None for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = [key, value]
        else:
            for i in range(index, self.size):
                if self.table[i] is None:
                    self.table[i] = [key, value]
                    return
                elif self.table[i][0] == key:
                    self.table[i][1] = value
                    return

    def get(self, key: int) -> int:
        index = self.hash_function(key)

        if self.table[index] is None:
            return -1
        else:
            for i in range(index, self.size):
                while self.table[i] is not None:
                    if self.table[i][0] == key:
                        return self.table[i][1]
                return -1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)

        if self.table[index] is None:
            return
        else:
            for i in range(index, self.size):
                while self.table[i] is not None:
                    if self.table[i][0] == key:
                        self.table[i] = None
                return

    def hash_function(self, key):
        """
        Use modulo hashing.
        """

        return key % self.size


if __name__ == "__main__":
    import random

    hashtable = ChainingHash()
    hashtable2 = OpenaddressHash()

    # put
    for i in range(500):
        data = random.randint(0, 500)
        hashtable.put(key=data, value=data)
        hashtable2.put(key=data, value=data)

    # get
    for i in range(500):
        value = hashtable.get(key=i)
        value2 = hashtable2.get(key=i)
        print(i, value, value2)

    # remove
    for i in range(500):
        hashtable.remove(key=i)
        hashtable2.remove(key=i)

    # get
    for i in range(500):
        value = hashtable.get(key=i)
        value2 = hashtable2.get(key=i)
        print(i, value, value2)
