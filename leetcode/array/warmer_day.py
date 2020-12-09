from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        out = []
        l = len(T)
        stack = []
        for i in reversed(range(l)):
            if not stack:
                out.append(0)
                stack.append([T[i], i])
            elif len(stack) > 0 and stack[-1][0] > T[i]:
                out.append(stack[-1][1] - i)
                stack.append([T[i], i])
            else:
                while len(stack) > 0 and stack[-1][0] <= T[i]:
                    stack.pop()
                if len(stack) == 0:
                    out.append(0)
                    stack.append([T[i], i])
                else:
                    out.append(stack[-1][1] - i)
                    stack.append([T[i], i])
        return out[::-1]


T = [73, 74, 75, 71, 69, 72, 76, 73]

print(Solution().dailyTemperatures(T))
