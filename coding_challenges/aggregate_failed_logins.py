import json


class Solution:
    def aggregateFailedLogins(self, data):
        logs = json.loads(data)
        EVENT = ["failed_login"]
        failedLogins = {}

        for log in logs:
            event_type, ip_address = (
                log.get("event_type"),
                log.get("ip_address"),
            )

            if event_type == EVENT[0]:
                if ip_address not in failedLogins:
                    failedLogins[ip_address] = 1
                else:
                    failedLogins[ip_address] += 1

        for ip, count in failedLogins.items():
            print(f"IP {ip} has {count} failed login attempts")


if __name__ == "__main__":
    solution = Solution()
    log_data = """
    [
    {"timestamp": "2024-12-25T12:34:56", "user": "admin", "event_type": "failed_login", "ip_address": "192.168.1.1"},
    {"timestamp": "2024-12-25T12:44:56", "user": "admin", "event_type": "failed_login", "ip_address": "192.168.1.1"},
    {"timestamp": "2024-12-25T12:56:01", "user": "admin", "event_type": "successful_login", "ip_address": "192.168.1.2"}
    ]
    """
    solution.aggregateFailedLogins(log_data)
