from webbrowser import get
import get_data
import json


def get_count_users(data: dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    sum = []
    for n in range(len(data['results'])):
        sum.append(data['results'][n]['name']['first'])
    return len(sum)


f = open('randomuser_data.json').read()
data = json.loads(f)
print(get_count_users(data))
