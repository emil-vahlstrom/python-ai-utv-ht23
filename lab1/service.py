import requests

# Documentation: https://random-word-api.herokuapp.com/home
apiEndpointTemplate = "https://random-word-api.herokuapp.com/word?number={number}"


def fetch_words(number: int) -> list[str]:
    apiEndpoint=apiEndpointTemplate.replace("{number}", str(number))
    #print(f'Connecting this following endpoint: {apiEndpoint}')

    r = requests.get(apiEndpoint)
    #print(f'status code: {r.status_code}')

    val = r.json()
    #print(val)
    #print(type(val))
    return val
