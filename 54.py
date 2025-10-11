class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top,bottom = 0, len(matrix)-1
        left,right = 0,len(matrix[0])-1

        while left<=right and top<=bottom:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            for j in range(top,bottom+1):
                result.append(matrix[j][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
            bottom-=1

            if right>=left:
                for j in range(bottom,top-1,-1):
                    result.append(matrix[j][left])
            left+=1
        return result
