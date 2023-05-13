from collections import defaultdict
# Ref NeetCode @ https://www.youtube.com/watch?v=TjFXEUCMqI8&t=728s
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    # Checking if current number is in row r
                    board[r][c] in rows[r]
                    # Checking if current number is in column c
                    or board[r][c] in cols[c]
                    # Checking if current number is in column r//3,c//3 (key that points to one of the 9 boxes.)
                    or board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True


sol = Solution()

print(sol.isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))