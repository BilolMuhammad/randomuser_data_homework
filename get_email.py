import get_data


def get_email(data: dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = []
    for n in range(len(data['results'])):
        emails.append(data['results'][n]['email'])
    return emails


data = get_data.get_data('randomuser_data.json')
print(get_email(data))
