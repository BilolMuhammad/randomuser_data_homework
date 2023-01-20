import get_data


def get_gender_users(data: dict) -> list:
    """
    Take the gender of the users and return the list.

    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}

    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    users_gender = []
    for n in range(len(data['results'])):
        users_gender.append(data['results'][n]['gender'])
    return users_gender


data = get_data.get_data('randomuser_data.json')
print(get_gender_users(data))
