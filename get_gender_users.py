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
    Male = {}
    Female = {}
    for n in range(len(data['results'])):
        if data['results'][n]['gender'] == 'male':
            Male['Male'] = 1
            Female['Female'] = 0
        else:
            Male['Male'] = 0
            Female['Female'] = 1
            male = Male.copy()
            female = Female.copy()
            users_gender.append(male)
            users_gender.append(female)

    return users_gender


data = get_data.get_data('randomuser_data.json')
print(get_gender_users(data))
