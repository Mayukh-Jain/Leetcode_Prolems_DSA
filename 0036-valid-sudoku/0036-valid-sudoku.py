class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r=[set() for _ in range(9)]
        c=[set() for _ in range(9)]
        b=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val=='.': continue
                bi=(i//3)*3+j//3
                if val in r[i] or val in c[j] or val in b[bi]: return False
                r[i].add(val)
                c[j].add(val)
                b[bi].add(val)
        
        return True