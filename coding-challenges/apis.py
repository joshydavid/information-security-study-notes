import requests


class Solution:
    def getTasks(self, apiURL, taskId):
        response = requests.get(f"{apiURL}/{taskId}")
        status_code, data = response.status_code, (
            response.json() if response.status_code == 200 else None
        )

        if status_code == 200:
            return data
        else:
            print(f"Request failed with status code {status_code}")

    def createTask(self, apiURL, taskData):
        response = requests.post(apiURL, json=taskData)
        status_code, data = response.status_code, (
            response.json() if response.status_code == 201 else None
        )

        if status_code == 201:
            return data
        else:
            print(f"Request failed with status code {status_code}")


if __name__ == "__main__":
    solution = Solution()
    URL = "https://jsonplaceholder.typicode.com/todos"

    print("******Get Tasks******")
    print()

    taskId = 1
    result = solution.getTasks(URL, taskId)
    print(result)
    print()

    taskId = 2
    result = solution.getTasks(URL, taskId)
    print(result)
    print()

    print("******Create Tasks******")
    print()

    taskData = {
        "userId": 1,
        "title": "Information Security Interview Preparation",
        "completed": False,
    }
    result = solution.createTask(URL, taskData)
    print(result)
    print()

    taskData = {
        "userId": 2,
        "title": "Software Engineer Interview Preparation",
        "completed": False,
    }
    result = solution.createTask(URL, taskData)
    print(result)
