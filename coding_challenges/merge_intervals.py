class Solution:
    def merge(self, intervals):
        """
        - https://leetcode.com/problems/merge-intervals/
        - can the input be empty?
        - are the values valid digits?
        - are the values sorted?
        """

        if not intervals:
            return intervals

        result = []
        intervals.sort(key=lambda interval: interval[0])

        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                prevStart, prevEnd = result[-1]
                result[-1] = [prevStart, max(prevEnd, interval[1])]

        return result


if __name__ == "__main__":
    solution = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = solution.merge(intervals)
    assert result == [[1, 6], [8, 10], [15, 18]]
    print(result)
    print("Test Case 1 Passed!")
    print()

    intervals = [[1, 4], [4, 5]]
    result = solution.merge(intervals)
    assert result == [[1, 5]]
    print(result)
    print("Test Case 2 Passed!")
    print()

    intervals = []
    result = solution.merge(intervals)
    assert result == []
    print(result)
    print("Test Case 3 Passed!")
