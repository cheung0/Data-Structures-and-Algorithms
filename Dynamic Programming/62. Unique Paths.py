"""
dynamic programming
time: O(m * n)
space: O(m * n)
remarks: All the cells one the first row and first col have exactly one unique path. For other cells, the number of unique paths it has is the number of unique ways to get to the cell above it and to the left of it.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * m for row in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):        
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        
        return paths[n - 1][m - 1]
                
