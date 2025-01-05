class Solution:
    def quickSort(self, nums):
        """
        - can the input be empty?
        - does it only contain valid numbers?
        - sort in ascending order/descending order?
        """

        if len(nums) <= 1:
            return nums

        pivot = nums[-1]
        left = [num for num in nums[:-1] if num <= pivot]
        right = [num for num in nums[:-1] if num > pivot]

        return self.quickSort(left) + [pivot] + self.quickSort(right)


if __name__ == "__main__":
    solution = Solution()

    arr = [10, 7, 8, 9, 1, 5]
    result = solution.quickSort(arr)
    assert result == [1, 5, 7, 8, 9, 10]
    print(result)
    print("Test Case 1 Passed!")
    print()

    arr = [50, 2, 12, 1, 0, 150, 125, 55]
    result = solution.quickSort(arr)
    assert result == [0, 1, 2, 12, 50, 55, 125, 150]
    print(result)
    print("Test Case 2 Passed!")
