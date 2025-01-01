class Solution:
    def twoSum(self, numbers, target):
        """
        - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
        - is the input sorted?
        - can the input be empty?
        """

        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return -1


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [1, 2]
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [2, 3, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [1, 3]
    print(result)
    print("Test Case 2 Passed!")
    print()

    nums = [-1, 0]
    target = -1
    result = solution.twoSum(nums, target)
    assert result == [1, 2]
    print(result)
    print("Test Case 3 Passed!")
    print()

    nums = []
    target = 6
    result = solution.twoSum(nums, target)
    assert result == -1
    print(result)
    print("Test Case 4 Passed!")
    print()
