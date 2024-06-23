# Brute force solution

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        for i in range(len(temperatures)):
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    out.append(j - i)
                    found = True
                    break
            if not found:
                out.append(0)
        return out

# Stack solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                top = stack.pop()[0]
                out[top] = i - top

            stack.append((i, t))
        
        return out