# Created by Jinwook Lim (Aiden Lim) at 8:02 PM 2021/06/22
__author__ = "Jinwook Lim (Aiden Lim)"

from typing import List

"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Runtime, memory
        # 32 ms	   14.4 MB
        return self.use_dfs(digits)
        # Runtime, memory
        # 28 ms	   14.2 MB
        # return self.use_product(digits)

    def use_dfs(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if not digits:
            return []

        result = []
        dfs(0, "")

        return result

    def use_product(self, digits: str) -> List[str]:
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        if not digits:
            return []

        alphabet_list = []
        for i in digits:
            alphabet_list.append([s for s in dic[i]])

        temp = list(itertools.product(*alphabet_list))

        result = []
        for r in temp:
            out = ""
            for i in r:
                out += i
            result.append(out)

        return result
