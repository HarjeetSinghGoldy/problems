from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.solveRec(res,nums,[])
        return res

    def solveRec(self, res, inputList, outputList):
        if len(inputList) == 0:
            res.append(outputList)
            return
        outPut1 = outputList[:]
        outPut2 = outputList[:]
        outPut2.append(inputList[0])
        inputList.pop(0)

        self.solveRec(res, inputList[:], outPut2)
        self.solveRec(res, inputList[:], outPut1)

        return

nums = [1,2,3]
print(Solution().subsets(nums))