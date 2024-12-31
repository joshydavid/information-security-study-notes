class Solution:
    def longestOnes(self, nums, k):
        """
        - https://leetcode.com/problems/max-consecutive-ones-iii/
        """

        zeroCount = 0
        maxOnes = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1

            # shrink the window
            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1

            maxOnes = max(maxOnes, r - l + 1)

        return maxOnes


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    result = solution.longestOnes(nums, k)
    assert result == 6
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    result = solution.longestOnes(nums, k)
    assert result == 10
    print(result)
    print("Test Case 2 Passed!")
