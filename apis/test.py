import requests


def test_api_endpoint(endpoint):
    # Send a HEAD request to the specified endpoint and return the response / not used yet
    response = requests.head(endpoint)
    return response
