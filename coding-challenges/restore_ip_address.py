class Solution:
    def restoreIpAddresses(self, s):
        """
        - https://leetcode.com/problems/restore-ip-addresses/
        - can s be empty?
        - does s only contain valid digits?
        """

        result, solution = [], []

        def backtrack(i):
            """
            valid IPv4
            - 4 parts
            - 3 periods
            - Each integer is between 0 and 255 (inclusive)
            - no leading 0
            """

            if i == len(s) and len(solution) == 4:  # ["255", "255", "11", "135"]
                result.append(".".join(solution))
                return result

            for length in range(1, 4):  # length = 1, 2, 3
                if i + length <= len(s):
                    segment = s[i : i + length]  # 2, 25, 255

                    if (len(segment) == 1 or segment[0] != "0") and (
                        0 <= int(segment) <= 255
                    ):
                        solution.append(segment)
                        backtrack(i + length)
                        solution.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    solution = Solution()

    s = "25525511135"
    result = solution.restoreIpAddresses(s)
    assert result == ["255.255.11.135", "255.255.111.35"]
    print(result)
    print("Test Case Passed!")
    print()
