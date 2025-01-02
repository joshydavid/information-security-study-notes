class Solution:
    def defangIPAddr(self, address):
        """
        - https://leetcode.com/problems/defanging-an-ip-address/
        - can the input be empty?
        - is the input always a valid IPv4 address?
        """

        PERIOD = "."
        NEW_CHAR = "[.]"
        defangedIP = []

        for ch in address:
            if ch == PERIOD:
                defangedIP.append(NEW_CHAR)
            else:
                defangedIP.append(ch)

        return "".join(defangedIP)


if __name__ == "__main__":
    solution = Solution()

    address = "1.1.1.1"
    result = solution.defangIPAddr(address)
    assert result == "1[.]1[.]1[.]1"
    print(result)
    print("Test Case Passed!")
    print()
