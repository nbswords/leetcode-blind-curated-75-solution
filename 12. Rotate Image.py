class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(i, n - 1 - i):
                left_top = matrix[i][j]  # tmp
                matrix[i][j] = matrix[-1-j][i]  # left_top = left_bottom
                # left_bottom = right_bottom
                matrix[-1-j][i] = matrix[-1-i][-1-j]
                # right_bottom = right_top
                matrix[-1-i][-1-j] = matrix[j][-1-i]
                matrix[j][-1-i] = left_top  # right_top = left_top

    # Solution 2 : Rotate 90 equal to turning the columns into rows then reversing them
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     matrix.reverse()
    #     for i in range(len(matrix)):
    #         for j in range(i, len(matrix)):
    #             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Time complexity : O(M), Space Complexity = O(1)
# Example : matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Pass 0 : [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# Pass 1 : [[7, 2, 1],
#           [4, 5, 6],
#           [9, 8, 3]]
# Pass 2 : [[7, 4, 1],
#           [8, 5, 2],
#           [9, 6, 3]]
# Output : [[7,4,1],[8,5,2],[9,6,3]]
