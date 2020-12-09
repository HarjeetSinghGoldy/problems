class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_level = []
        num = 0

        for char in s:
            if char.isnumeric():
                num = num * 10 + int(char)
            if char.isalpha():
                cur_level.append(char)
            if char == "[":
                stack.append((num, [*cur_level]))
                cur_level = []
                num = 0
            if char == "]":
                prev_level_num, prev_level = stack.pop()
                cur_level_string = "".join(cur_level)
                cur_level = [*prev_level, prev_level_num * cur_level_string]

        return "".join(cur_level)

s = "3[a]2[bc]"
s = "3[a2[c]]"

print(Solution().decodeString(s))