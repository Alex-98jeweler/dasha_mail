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

    def lists_get(self, list_id: int = None, merge_json: int = None):
        """
        :param list_id: получить определенную группу
        :param merge_json: вывод сериализованныъ доп. полей 
        """
        params = {}
        if list_id:
            params['list_id'] = list_id
        return self.__send_request("lists.get", params)

    def lists_add(self, name='', **params):
        params.update({'name': name})
        return self.__send_request("lists.add", params)

    def lists_update(self, list_id=None, **params):
        params.update({'list_id': list_id})
        return self.__send_request('lists.update', params)

    def lists_delete(self, list_id, **params):
        params.update({'list_id': list_id})
        return self.__send_request('lists.delete', params)

