class Solution:
    def validIPAddress(self, queryIP):
        """
        - https://leetcode.com/problems/validate-ip-address/
        - can the input be empty?
        - is the input always a valid IPv4 or IPv6?
        """

        VALID_IPv4 = "IPv4"
        VALID_IPv6 = "IPv6"
        NEITHER = "Neither"

        if queryIP.count(".") == 3 and self.isValidIPv4(queryIP):
            return VALID_IPv4
        elif queryIP.count(":") == 7 and self.isValidIPv6(queryIP):
            return VALID_IPv6
        else:
            return NEITHER

    def isValidIPv4(self, IP):
        """
        - contains 4 parts
        - contains 3 periods
        - each part 0 <= x <= 255
        - each part is digit
        - no leading zeroes
        """

        parts = IP.split(".")
        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit() or not (0 <= int(part) <= 255):
                return False

            # "01" -> 1 -> "1"
            if part != str(int(part)):
                return False

        return True

    def isValidIPv6(self, IP):
        """
        - contains 8 parts
        - the length of each part is between 1 and 4 (inclusive)
        - all the character in the part must fulfill the hexadecimal criteria
        - leading zero is OK
        """

        parts = IP.split(":")
        if len(parts) != 8:
            return False

        HEXA_DECIMAL = "0123456789abcdefABCDEF"

        for part in parts:
            if not (1 <= len(part) <= 4):
                return False

            if not all(ch in HEXA_DECIMAL for ch in part):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    queryIP = "172.16.254.1"
    result = solution.validIPAddress(queryIP)
    assert result == "IPv4"
    print(result)
    print("Test Case Passed!")
    print()
