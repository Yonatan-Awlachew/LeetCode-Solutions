class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for num in matrix:
            total=0
            temp=[]
            for x in num:
                total+=x
                temp.append(total)
            self.sums.append(temp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1,row2+1):
            row_sum = self.sums[r][col2]
            row_sum -= self.sums[r][col1-1] if col1>0 else 0
            total+=row_sum
        return total
