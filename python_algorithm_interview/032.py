# Created by Jinwook Lim (Aiden Lim) at 7:21 PM 2021/06/22
__author__ = "Jinwook Lim (Aiden Lim)"

from typing import List

"""
https://leetcode.com/problems/number-of-islands/
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.len = len(grid)

        count = 0
        for i in range(self.len):
            for j in range(self.len):
                if grid[i][j] == '1':
                    # start dfs
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= self.len or j < 0 or j >= self.len or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
