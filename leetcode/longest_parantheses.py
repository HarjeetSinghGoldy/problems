class Solution:
    def longestValidParentheses(self, s: str) -> int:
        leftBracketCount = 0
        rightBracketCount = 0
        longestValidBracketLength = 0

        for i in range(len(s)):
            if s[i] == '(':
                leftBracketCount = leftBracketCount + 1
            if s[i] == ')':
                rightBracketCount = rightBracketCount + 1
            if leftBracketCount == rightBracketCount:
                longestValidBracketLength = max(longestValidBracketLength, 2 * leftBracketCount)
            if rightBracketCount > leftBracketCount:
                leftBracketCount = 0
                rightBracketCount = 0

        leftBracketCount = 0
        rightBracketCount = 0
        for i in reversed(range(len(s))):
            if s[i] == '(':
                leftBracketCount = leftBracketCount + 1
            if s[i] == ')':
                rightBracketCount = rightBracketCount + 1
            if leftBracketCount == rightBracketCount:
                longestValidBracketLength = max(longestValidBracketLength, 2 * leftBracketCount)
            if leftBracketCount > rightBracketCount:
                leftBracketCount = 0
                rightBracketCount = 0

        return longestValidBracketLength


s = "(()"
# s = ")()())"
# s = ")()(())"
print(Solution().longestValidParentheses(s))






