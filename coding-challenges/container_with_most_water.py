class Solution:
    def maxArea(self, height):
        """
        - https://leetcode.com/problems/container-with-most-water
        - can the input be null?
        """

        maxWater = 0
        l, r = 0, len(height) - 1

        while l < r:
            currArea = (r - l) * min(height[l], height[r])
            maxWater = max(maxWater, currArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxWater


if __name__ == "__main__":
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = solution.maxArea(height)
    assert result == 49
    print(result)
    print("Test Case 1 Passed!")
    print()

    height = [1, 1]
    result = solution.maxArea(height)
    assert result == 1
    print(result)
    print("Test Case 2 Passed!")
    print()
