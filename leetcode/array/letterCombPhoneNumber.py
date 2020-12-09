from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyPadHash = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def solveRec(combination, numbers):
            if len(numbers) == 0:
                out.append(combination)
            else:
                for letter in keyPadHash[numbers[0]]:
                    solveRec(combination + letter, numbers[1:])
        out = []
        if digits:
            solveRec("",digits)

        return out


digits = "9999"

print(len(Solution().letterCombinations(digits)))
