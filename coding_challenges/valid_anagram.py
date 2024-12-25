class Solution:
    def isAnagram(self, s, t):
        """
        - https://leetcode.com/problems/valid-anagram
        - can the input be empty?
        - are the inputs in lowercase or uppercase?
        - return true if t is an anagram of s
        """

        if len(t) != len(s):
            return False

        map_s = {}
        for ch in s:
            if ch not in map_s:
                map_s[ch] = 1
            else:
                map_s[ch] += 1

        for ch in t:
            if ch not in map_s:
                return False
            else:
                map_s[ch] -= 1

        for value in map_s.values():
            if value != 0:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    assert result == True
    print(result)
    print("Test Case 1 Passed!")
    print()

    s = "rat"
    t = "car"
    result = solution.isAnagram(s, t)
    assert result == False
    print(result)
    print("Test Case 2 Passed!")
    print()
