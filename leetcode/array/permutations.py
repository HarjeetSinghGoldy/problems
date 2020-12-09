from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrackPermutaions(result,path,k,choices):
            if k == 0:
                result.append(path)
            else:
                for i in range(len(choices)):
                    backTrackPermutaions(result, path+[choices[i]], k - 1, choices[:i] + choices[i+1:])
        result = []
        backTrackPermutaions(result , [], len(nums), nums)
        return result



arrr = [1,2,3]

print(Solution().permute(arrr))
