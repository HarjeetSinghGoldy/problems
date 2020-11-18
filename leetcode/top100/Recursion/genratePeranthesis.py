from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        leftBracket = n
        rightBracket = n
        outputString = ""
        resultArr = []
        self.recSolve(leftBracket, rightBracket, outputString, resultArr)
        return resultArr

    def recSolve(self, leftBracket, rightBracket, outputString, resultArr):

        if leftBracket == 0 and rightBracket == 0:
            resultArr.append(outputString)
            return

        if leftBracket != 0:
            op1 = outputString
            op1 = op1 + "("
            self.recSolve(leftBracket - 1, rightBracket, op1, resultArr)
        if rightBracket > leftBracket:
            op2 = outputString
            op2 = op2 + ")"
            self.recSolve(leftBracket, rightBracket - 1, op2, resultArr)
            return


print(Solution().generateParenthesis(3))
