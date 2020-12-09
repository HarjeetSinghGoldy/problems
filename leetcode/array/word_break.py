from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = [False] * len(s)  # mark the indexes we visited
        result = [False] * len(s)  # cache the results for the visited indexes

        def helper(string, i, word_dict_hash):

            if i == len(string):
                return True

            if visited[i]:
                return result[i]
            start = i
            for end in range(i, len(string)):
                cur_window = string[start:end + 1]
                if cur_window in word_dict_hash:
                    if helper(string, end + 1, word_dict_hash):
                        visited[i] = True
                        result[i] = True
                        return True

            # cache False results
            visited[i] = True
            result[i] = False
            return False

        word_dict_hash = set(wordDict)
        resultRet = helper(s, 0, word_dict_hash)
        return resultRet

s = "leetcode"
wordDict = ["leet", "code"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(Solution().wordBreak(s,wordDict))