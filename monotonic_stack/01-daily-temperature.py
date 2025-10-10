# difficulty : medium
# time taken : ALOT but kinda learned monotonic stack so worth it

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [-1]*len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            if not stack:
                answer[i] = 0
                stack.append({temperatures[i]:i})
                continue
            while True:
                key, idx = next(iter(stack[-1].items()))
                if key > temperatures[i]:
                    answer[i] = idx - i
                    stack.append({temperatures[i]:i})
                    break
                stack.pop()
                if not stack:
                    answer[i] = 0
                    stack.append({temperatures[i]:i})
                    break
        return answer

