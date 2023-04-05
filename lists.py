from typing import Optional
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
    
    def get_unsubscribed(self, **params):
        return self.api_client.send_request("lists.get_unsubscribed", params)
    
    def get_complaints(self, **params):
        return self.api_client.send_request("lists.get_complaints", params)

    def member_activity(self, email, filter: Optional[str] = None):
        params = {
            "email": email,
        }
        if filter:
            params['filter'] = filter
        return self.api_client.send_request('lists.member_activity', params=params)

    def upload(self, list_id, index_email: int=0, file: bytes=None, file_type: str = None, **params):
        if file:
            file = {'import-file': file}
            params.update(
                {
                'type': file_type, 
                'email': index_email
                }
            )
        params.update({'list_id': list_id})
        return self.api_client.send_request('lists.upload', params=params, files=file)
    
    def add_member(self, list_id, email, **params):
        params['list_id'] = list_id
        params['email'] = email
        return self.api_client.send_request("lists.add_member", params)

    def add_member_batch(self, 
                         list_id, 
                         batch, 
                         **params):
        params['list_id'] = list_id
        params['batch'] = batch
        return self.api_client.send_request('lists.add_member_batch', params)

    def update_member(self, 
                      member_id: int = None, 
                      email: str = None, 
                      list_id: int = None, 
                      **params):
        params['member_id'] = member_id
        params['email'] = email
        params['list_id'] = list_id
        return self.api_client.send_request('lists.update_member', params)

    def delete_member(self):
        pass

    def unsubscribe_member(self):
        pass

    def move_member(self):
        pass

    def copy_member(self):
        pass

    def add_merge(self):
        pass

    def update_merge(self):
        pass

    def delete_merge(self):
        pass

    def last_status(self):
        pass

    def get_import_history(self):
        pass

    def check_emai(self):
        pass


    