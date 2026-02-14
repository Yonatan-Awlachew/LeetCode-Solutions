class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        Empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    Empty.append((r,c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    index = (r//3)*3+(c//3)
                    boxes[index].add(board[r][c])
        def backtrack():
            if not Empty:return True
            Empty.sort(key=lambda pos:len(
                set(map(str,range(1,10)))-
                rows[pos[0]]-
                cols[pos[1]]-
                boxes[(pos[0] // 3) * 3 + (pos[1] // 3)]))

            r,c = Empty.pop(0)
            index = (r//3)*3 + (c//3)
            candidates = set(map(str,range(1,10)))-rows[r]-cols[c]-boxes[index]
            for num in candidates:
                board[r][c]=num
                rows[r].add(num)
                cols[c].add(num)
                boxes[index].add(num)

                if backtrack():return True

                board[r][c]="."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[index].remove(num)
            Empty.insert(0,(r,c))
            return False
        backtrack()
                    
