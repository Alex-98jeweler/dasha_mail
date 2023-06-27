import requests

from dasha_mail.exceptions import DashaMailException
from dasha_mail.errors import ERRORS
from dasha_mail.configuration import Configuration


class DashaApiClient:

    def __init__(self,) -> None:
        self.settings = Configuration()

    def send_request(self, method, params=None, files=None):
        response = requests.post(
                                f"{self.settings.api_url}?method={method}&api_key={self.settings.api_key}",
                                data=params,
                                files=files
                                )
        data = self.__parse_response(response.json())
        return data

    def __parse_response(self, json: dict):
        response = json.get('response')
        msg = response.get('msg')
        err_code = msg.get('err_code')
        if err_code == 0:
            return response['data']
        else:
            raise DashaMailException(ERRORS[err_code].capitalize())
