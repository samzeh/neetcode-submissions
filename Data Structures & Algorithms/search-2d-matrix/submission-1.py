class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        colLength = len(matrix[0])

        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                row = i-1
                break
            else:
                row = i
        
        for i in range(colLength):
            if target == matrix[row][i]:
                return True
            elif target > matrix[row][i]:
                i += 1
            else:
                return False
        
        return False
        