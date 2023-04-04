import requests

from exceptions import DashaMailException
from errors import ERRORS

class DashaApiClient:

    def __init__(self, api_key) -> None:
        self.__api_key = api_key
        self.__api_url = "https://api.dashamail.ru/"

    def __send_request(self, method, params=None):
        response = requests.post(f"{self.__api_url}?method={method}&api_key={self.__api_key}", params)
        data = self.__parse_response(response.json())
        return data

    def __parse_response(self, json: dict):
        response = json.get('response')
        msg = response.get('msg')
        err_code = msg.get('err_code')
        if err_code == 0:
            return response['data']
        else:
            raise DashaMailException(ERRORS[err_code])
