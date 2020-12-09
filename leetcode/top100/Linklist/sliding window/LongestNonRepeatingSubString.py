class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = k = 0
        n = len(s)
        if n == 0:
            return 0
        ans = 0
        hashMap = {}

        while i < n and j < n:
            if s[j] not in hashMap:
                hashMap[s[j]] = 1
                ans = max (ans, j-i+1)
                j = j + 1
            else:
                del hashMap[s[i]]
                i = i + 1

        return ans







s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))