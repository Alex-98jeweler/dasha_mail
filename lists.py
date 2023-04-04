from io import TextIOWrapper
from base_entity import BaseEntity


class Lists(BaseEntity):

    name = 'list'
    plural_name = 'lists'

    def add(self, name, **params):
        params.update({'name': name})
        return self.api_client.send_request("lists.add", params)
    
    def get_members(self, list_id, **params):
        params.update({'list_id': list_id})
        return self.api_client.send_request('lists.get_members', params)
    
    def upload(self, list_id, file: bytes = None, **params):
        if file:
            file = {'import-file': file}
        params.update({'list_id': list_id,})
        return self.api_client.send_request('lists.upload', params=params, files=file)
    