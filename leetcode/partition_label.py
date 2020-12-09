from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        out = []
        last_hash = {}

        for i,char in enumerate(S):
            last_hash[char] = i
        anchor = 0
        j = 0
        for i, char in enumerate(S):
            j = max(j, last_hash[char])
            if i == j:
                out.append(i - anchor+1)
                anchor = i + 1

        return out


S = "ababcbacadefegdehijhklij"

print((Solution().partitionLabels(S)))



