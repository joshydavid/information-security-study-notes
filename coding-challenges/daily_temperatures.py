class Solution:
    def dailyTemperatures(self, temperatures):
        """
        - https://leetcode.com/problems/daily-temperatures/
        - can the input be null?
        """

        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prevIndex, _ = stack.pop()
                answer[prevIndex] = i - prevIndex

            stack.append((i, t))

        return answer


if __name__ == "__main__":
    solution = Solution()

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    result = solution.dailyTemperatures(temperatures)
    assert result == [1, 1, 4, 2, 1, 1, 0, 0]
    print(result)
    print("Test Case 1 Passed!")
    print()

    temperatures = [30, 40, 50, 60]
    result = solution.dailyTemperatures(temperatures)
    assert result == [1, 1, 1, 0]
    print(result)
    print("Test Case 2 Passed!")
    print()

    temperatures = [30, 60, 90]
    result = solution.dailyTemperatures(temperatures)
    assert result == [1, 1, 0]
    print(result)
    print("Test Case 3 Passed!")
    print()
