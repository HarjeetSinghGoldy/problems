from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        out = []
        bit_hash = {0: 0}
        for i in range(n+1):
            if i % 2 == 0:
                bit_hash[i] = bit_hash[i / 2]
            else:
                bit_hash[i] = 1 + bit_hash[i - 1]

        for i in range(len(bit_hash)):
            out.append(bit_hash[i])
        return out


n = 2
print(Solution().countBits(n))
