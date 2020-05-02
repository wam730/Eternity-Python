class Solution(object):

    def solveNQueens(self,n):
        self.helper([-1]*n,0,n)
    def helper(self,columnPositions,rowIndex,n):
        if rowIndex == n:
            self.printSolution(columnPositions,n)
            return
        for column in range(n):
            columnPositions[rowIndex] = column
            if self.isValid(columnPositions,rowIndex):
                self.helper(columnPositions,rowIndex+1,n)
    def isValid(self,columnPositions,rowIndex):
        for i in range(rowIndex):
            if columnPositions[i] == columnPositions[rowIndex]:
                return False
            elif abs(columnPositions[i]-columnPositions[rowIndex])==rowIndex - i:
                return False
        return True
    def printSolution(self,columnPositions,n):
        for row in range(n):
            line = ""
            for column in range(n):
                if columnPositions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print('\n')

Solution().solveNQueens(8)