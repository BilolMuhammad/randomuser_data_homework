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
    dic = {}
    list_data = []
    for n in range(len(data['results'])):
        dic['first_name'] = data['results'][n]['name']['first']
        dic['last_name'] = data['results'][n]['name']['last']
        dic['phone_number'] = data['results'][n]['phone']
        dictionary = dic.copy()
        list_data.append(dictionary)
    return list_data


data = get_data.get_data('randomuser_data.json')
print(get_users_data(data))
