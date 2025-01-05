class Solution:
    def bubbleSort(self, nums):
        """
        - can the input be empty?
        - does it only contain valid numbers?
        - sort in ascending order/descending order?
        """

        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums


if __name__ == "__main__":
    solution = Solution()

    arr = [10, 7, 8, 9, 1, 5]
    result = solution.bubbleSort(arr)
    assert result == [1, 5, 7, 8, 9, 10]
    print(result)
    print("Test Case 1 Passed!")
    print()

    arr = [50, 2, 12, 1, 0, 150, 125, 55]
    result = solution.bubbleSort(arr)
    assert result == [0, 1, 2, 12, 50, 55, 125, 150]
    print(result)
    print("Test Case 2 Passed!")
