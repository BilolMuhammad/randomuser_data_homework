import get_data


def get_users_data(data: dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.

    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    data_user = []
    for n in range(len(data['results'])):
        data_user.append(data['results'][n]['name']['first'])
        data_user.append(data['results'][n]['name']['last'])
        data_user.append(data['results'][n]['phone'])
    return data_user


data = get_data.get_data('randomuser_data.json')
print(get_users_data(data))
