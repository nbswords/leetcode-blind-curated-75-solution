class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not any(matrix):
            return []
        m, n = len(matrix), len(matrix[0])
        r, c, dr, dc = 0, 0, 0, 1  # row, col and direction row, col
        result = []
        for _ in range(m*n):
            result.append(matrix[r][c])
            matrix[r][c] = None  # initialize
            # Wheb bump into m*n border
            if matrix[(r + dr) % m][(c + dc) % n] is None:
                dr, dc = dc, -dr
            # walk
            r += dr
            c += dc
            print(r, dr)
            print(c, dc)
        return result
