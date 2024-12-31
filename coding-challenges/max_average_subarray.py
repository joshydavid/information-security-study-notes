class Solution:
    def findMaxAverage(self, nums, k):
        """
        - https://leetcode.com/problems/maximum-average-subarray-i/
        """

        maxSum = winSum = sum(nums[:k])

        for i in range(k, len(nums)):
            winSum = winSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, winSum)

        return maxSum / k


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    result = solution.findMaxAverage(nums, k)
    assert result == 12.75
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [5]
    k = 1
    result = solution.findMaxAverage(nums, k)
    assert result == 5.0
    print(result)
    print("Test Case 2 Passed!")
