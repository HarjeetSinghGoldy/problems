class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        rows = ["" for _ in range(numRows)]
        start = 0
        dir = -1

        for elm in s:
            rows[start] = rows[start] + elm

            if start  == 0 or start == numRows -1:
                dir = dir * -1

            start = start + dir

        return "".join(rows)



s= "PAYPALISHIRING"
row = 3

print(Solution().convert(s,row))