class Solution:
    def binarySearch(self, nums, target):
        """
        - https://leetcode.com/problems/binary-search/
        - can the input be empty?
        - is the input always sorted?
        - what to return if target is not found?
        """

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = solution.binarySearch(nums, target)
    assert result == 4
    print(result)
    print("Test Case Passed!")
    print()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = solution.binarySearch(nums, target)
    assert result == -1
    print(result)
    print("Test Case Passed!")
    print()
