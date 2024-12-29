class Solution:
    def findDuplicate(self, nums):
        # Floyd’s Tortoise and Hare Algorithm (Cycle Detection)
        slow, fast = nums[0], nums[0]

        # find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find starting point aka the duplicate number
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 3, 4, 2, 2]
    result = solution.findDuplicate(nums)
    assert result == 2
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [3, 1, 3, 4, 2]
    result = solution.findDuplicate(nums)
    assert result == 3
    print(result)
    print("Test Case 2 Passed!")
    print()

    nums = [3, 3, 3, 3, 3]
    result = solution.findDuplicate(nums)
    assert result == 3
    print(result)
    print("Test Case 3 Passed!")
    print()
