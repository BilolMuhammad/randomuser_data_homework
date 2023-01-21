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
    dic = {
        'Male': 0,
        'Female': 0
    }
    for n in range(len(data['results'])):
        if data['results'][n]['gender'] == 'male':
            dic['Male'] = 1
            dic['Female'] = 0
        else:
            dic['Male'] = 0
            dic['Female'] = 1
        dictionary = dic.copy()
        users_gender.append(dictionary)
    return users_gender


data = get_data.get_data('randomuser_data.json')
print(get_gender_users(data))
