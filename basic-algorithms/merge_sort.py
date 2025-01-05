class Solution:
    def mergeSort(self, nums):
        """
        - https://leetcode.com/problems/sort-an-array/
        - can the input be empty?
        - does it only contain valid numbers?
        - sort in ascending order/descending order?
        """

        # base case, already sorted
        if len(nums) <= 1:
            return nums

        # divide the array into two halves
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        # merge the two halves
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # append the remaining elements
        # method 1
        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        # method 2
        # result.extend(left[i:])
        # result.extend(right[j:])

        return result


if __name__ == "__main__":
    solution = Solution()

    arr = [10, 7, 8, 9, 1, 5]
    result = solution.mergeSort(arr)
    assert result == [1, 5, 7, 8, 9, 10]
    print(result)
    print("Test Case Passed!")
