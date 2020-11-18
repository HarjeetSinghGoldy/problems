from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashMap and hashMap[compliment] != i:
                result.append(i)
                result.append(hashMap[compliment])
                hashMap.pop(nums[i])
        return result



def main():
    nums = [0,4,3,0]
    target = 0
    print(Solution().twoSum(nums,target))


if __name__ == '__main__':
    main()
