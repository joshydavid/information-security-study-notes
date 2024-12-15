import re


class Solution:
    def isStrongPassword(self, password):
        # Password should have at
        # least 8 characters,
        # include both upper and lowercase letters, and
        # contain a digit and
        # contain a special character

        if len(password) < 8:
            return False

        validPatterns = [
            (r"[A-Z]", "Password should contain at least one upper case"),
            (r"[a-z]", "Password should contain at least one lower case"),
            (r"\d", "Password should contain at least one digit"),
            (r"\W_", "Password should contain a special character"),
        ]

        for pattern, message in validPatterns:
            if not re.search(pattern, password):
                print(f"Weak password: {message}")
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    password = "Password123"
    result = solution.isStrongPassword(password)
    print(result)
