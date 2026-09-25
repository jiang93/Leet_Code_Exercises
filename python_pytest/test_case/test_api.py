import pytest
import requests

@pytest.mark.api
def test_duckduckgo_request():
    # arrange
    url = "https://duckduckgo.com/?q=python+programming&format=json"

    # act 
    response = requests.get(url)
    #print(dir(response))
    #print(response.status_code)

    # assert
    assert response.status_code in [200, 202]
