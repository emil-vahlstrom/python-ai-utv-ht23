# https://pypi.org/project/requests2/
import requests

# Documentation: https://random-word-api.herokuapp.com/home
apiEndpointTemplate = "https://random-word-api.herokuapp.com/word?number={number}"


def fetch_words(number: int) -> list[str]:
    """
    Fetches random words
    Parameters:
        number (int): How many words to fetch

    Returns:
        list[str]: A list of random words 
    """
    apiEndpoint = apiEndpointTemplate.replace("{number}", str(number))
    # print(f'Connecting this following endpoint: {apiEndpoint}')
    print(f'Fetching {number} words from the interwebs...')
    r = requests.get(apiEndpoint)
    if r.status_code >= 400:
        print(f'Something went horribly wrong during request')
        r.raise_for_status()
    return r.json()
