class Solution:
    def threeSum(self, nums):
        """
        - https://leetcode.com/problems/3sum/
        - is the input sorted?
        - can the input be empty?
        """

        nums.sort()
        result = []

        for i in range(len(nums)):
            # avoid duplicate in the final result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # pointers
            j = i + 1
            k = len(nums) - 1

            # 2 pointers
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    solution = [nums[i], nums[j], nums[k]]
                    result.append(solution)
                    j += 1

                    # skip duplicate after finding triplets
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result


if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)
    assert result == [[-1, -1, 2], [-1, 0, 1]]
    print(result)
    print("Test Case 1 Passed!")
    print()

    nums = [0, 1, 1]
    result = solution.threeSum(nums)
    assert result == []
    print(result)
    print("Test Case 2 Passed!")
    print()

    nums = [0, 0, 0]
    result = solution.threeSum(nums)
    assert result == [[0, 0, 0]]
    print(result)
    print("Test Case 3 Passed!")
    print()
