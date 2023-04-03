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
    
    def campaigns_get(self, campaign_id: int=None, merge_json: int = None, **params):
        if campaign_id:
            params.update({'campaign_id':campaign_id})
        return self.__send_request('campaigns.get', params) # Возвращается массив
    
    def campaigns_create(self, list_id: int=None, **params):
        params.update({'list_id':list_id})
        return self.__send_request('campaigns.create', params)   # Возвращается ID созданной рассылки
    
    def campaigns_create_auto(self, list_id: int=None, **params):
        if list_id:
            params.update({'list_id':list_id})
        return self.__send_request('campaigns.create_auto', params)
    
    def campaigns_update(self, campaign_id: int=None, **params):
        params.update({'campaign_id' : campaign_id})
        return self.__send_request('campaigns.update', params)
    
    def campaigns_update_auto(self, campaign_id: int=None, **params):
        params.update({'campaign_id' : campaign_id})
        return self.__send_request('campaigns.update_auto', params)
    
    def campaigns_delete(self, campaign_id: int=None):
        return self.__send_request('campaigns.delete',{'campaign_id':campaign_id})
    
    def campaigns_attach(self, campaign_id: int=None, url: str=None, **params):
        params.update({'campaign_id':campaign_id, 'url': url})
        return self.__send_request('campaigns.attach', params)
    
    def campaigns_get_attachments(self, campaign_id: int=None):
        return self.__send_request('campaigns.get_attachments',{'campaign_id':campaign_id})
    
    def campaigns_delete_attachments(self, campaign_id: int=None, id: int=None):
        params = {'campaign_id' : campaign_id, 'id' : id}
        return self.__send_request('campaigns.delete_attachment', params)
    
    def campaigns_get_templates(self, **params):
        return self.__send_request('campaigns.get_templates', params)
    
    def campaigns_get_saved_templates(self, **params):
        return self.__send_request('campaigns.get_saved_templates', params)
    
    def campaigns_add_template(self, name: str=None, template: str=None):
        params = {'name':name, 'template':template}
        return self.__send_request('campaigns.add_template', params)
    
    def campaigns_delete_template(self, id: int=None):
        return self.__send_request('campaigns.delete_template', {'id':id})

    def campaigns_force_auto(self, campaign_id:int=None, member_id:int=None, **params): 
        params.update({'campaign_id':campaign_id, 'member_id':member_id})
        return self.__send_request('campaigns.force_auto', params)
    
    def campaigns_multi_create(self, json: dict=None):
        return self.__send_request('campaigns.multi_create',{'json':json})
    
    def campaigns_multi_get(self, campaign_id):
        return self.__send_request('campaigns.multi_get', {'campaign_id':campaign_id})
    
    def campaigns_multi_update(self, campaign_id: int=None, json: dict=None):
        return self.__send_request('campaign.multi_update', {'campaign_id':campaign_id, 'json':json})
    
    def campaigns_get_folder(self, name: str=None, id: int=None ):
        params = {'name':name,'id':id}
        return self.__send_request('campaigns.get_folder', params)
    
    def campaigns_move_to_folder(self, campaign_id :int=None, folder_id:int=None):
        params = {'campaign_id':campaign_id, 'folder_id':folder_id}
        return self.__send_request('campaigns.move_to_folder', params)
    
    def campaigns_pause(self, campaign_id):
        return self.__send_request('campaigns.pause', {'campaign_id':campaign_id})
    
    def campaigns_restart_paused(self, campaign_id):
        return self.__send_request('campaigns.restart_paused', {'campaign_id':campaign_id})
    
campaigns = DashaApiClient(api_key='047dc2e62b1694e88aeca1da2dc87837')
resp = campaigns.campaigns_get_saved_templates()
print(resp)

        