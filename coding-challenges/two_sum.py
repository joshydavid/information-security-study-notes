class Solution:
    def twoSum(self, nums, target):
        """
        - https://leetcode.com/problems/two-sum/
        - can the input be empty?
        - are the numbers sorted?
        - does it only contain valid numbers?
        """

        if not nums:
            return nums

        mapping = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement not in mapping:
                mapping[num] = i
            else:
                return [mapping[complement], i]


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [0, 1]
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [1, 2]
    print(result)
    print("Test Case 2 Passed!")
    print()

    nums = []
    target = 6
    result = solution.twoSum(nums, target)
    assert result == []
    print(result)
    print("Test Case 3 Passed!")
    print()
