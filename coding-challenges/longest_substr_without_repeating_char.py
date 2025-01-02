class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        - https://leetcode.com/problems/longest-substring-without-repeating-characters/
        """

        longest = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            # shrink the window
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            length = r - l + 1
            longest = max(longest, length)
            charSet.add(s[r])

        return longest


if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3
    print(result)
    print("Test Case 1 Passed!")
    print()

    s = "bbbbb"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 1
    print(result)
    print("Test Case 2 Passed!")
    print()

    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    assert result == 3
    print(result)
    print("Test Case 3 Passed!")
