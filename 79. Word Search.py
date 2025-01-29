class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(x: int, y: int, i: int = 0):
            if board[x][y] != word[i]:
                return False
            if i == len(word)-1:
                return True
            value = board[x][y]
            board[x][y] = '#'
            # Search right, left, up, down
            for r, c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                if 0 <= r < m and 0 <= c < n and DFS(r, c, i + 1):
                    return True
            board[x][y] = value
            return False

        if not word or not any(board):
            return False
        m, n = len(board), len(board[0])
        return any(DFS(x, y) for x in range(m) for y in range(n))
