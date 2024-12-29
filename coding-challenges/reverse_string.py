class Solution:
    def reverseStr(self, str):
        """
        - https://leetcode.com/problems/reverse-string/
        - can the input be empty?
        """

        if not str:
            return str

        left, right = 0, len(str) - 1
        while left < right:
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1

        return str


if __name__ == "__main__":
    solution = Solution()

    s = ["h", "e", "l", "l", "o"]
    result = solution.reverseStr(s)
    assert result == ["o", "l", "l", "e", "h"]
    print(result)
    print("Test Case 1 Passed!")
    print()

    s = []
    result = solution.reverseStr(s)
    assert result == []
    print(result)
    print("Test Case 2 Passed!")
