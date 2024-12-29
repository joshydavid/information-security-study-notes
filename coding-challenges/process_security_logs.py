import json


class Solution:
    def processSecurityLogs(self, data):
        logs = json.loads(data)
        EVENT = ["failed_login", "successful_login"]

        for log in logs:
            timestamp, user, event_type, ip_address = (
                log.get("timestamp"),
                log.get("user"),
                log.get("event_type"),
                log.get("ip_address"),
            )

            if event_type == EVENT[0]:
                print(
                    f"Failed login attempt by user {user} from IP {ip_address} at {timestamp}"
                )
            else:
                print(
                    f"User {user} logged in successfully from IP {ip_address} at {timestamp}"
                )


if __name__ == "__main__":
    solution = Solution()
    log_data = """
    [
    {"timestamp": "2024-12-25T12:34:56", "user": "admin", "event_type": "failed_login", "ip_address": "192.168.1.1"},
    {"timestamp": "2024-12-25T12:44:56", "user": "admin", "event_type": "failed_login", "ip_address": "192.168.1.1"},
    {"timestamp": "2024-12-25T12:56:01", "user": "admin", "event_type": "successful_login", "ip_address": "192.168.1.2"}
    ]
    """
    solution.processSecurityLogs(log_data)
