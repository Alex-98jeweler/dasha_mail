from typing import Optional, Union
from dasha_mail.base_entity import BaseEntity


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

    def delete_member(self, member_id):
        params = {'member_id': member_id}
        return self.api_client.send_request('lists.delete_member', params)

    def unsubscribe_member(
                            self, 
                            member_id: int = None, 
                            email: str = None, 
                            list_id: int=None
                           ):
        params = {
            'member_id': member_id,
            'email': email,
            'list_id': list_id
        }
        return self.api_client.send_request('lists.unsubscribe_member', params)

    def move_member(self, member_id: int, list_id: int):
        params = {
            'member_id': member_id,
            'list_id': list_id
        }
        return self.api_client.send_request('lists.move_member', params)

    def copy_member(self, member_id: int, list_id: int):
        params = {
            'member_id': member_id,
            'list_id': list_id
        }
        return self.api_client.send_request('lists.copy_member', params)

    def add_merge(self,
                  list_id,
                  type: str,
                  choices: list,
                  **params):
        buf_params = {
            'list_id': list_id,
            'type': type,
            'choices': choices
        }
        params.update(buf_params)
        return self.api_client.send_request('lists.add_merge', params)
        

    def update_merge(self, list_id: int, merge_id: int, **params):
        buf_params = {
            'list_id': list_id, 
            'merge_id': merge_id,
        }
        params.update(buf_params)
        return self.api_client.send_request('lists.update_merge', params)

    def delete_merge(self, list_id: int, merge_id: int):
        params = {
            'list_id': list_id,
            'merge_id': merge_id
        }
        return self.api_client.send_request('lists.delete_merge', params)
        

    def last_status(self, email, list_id: int = None):
        params = {
            'email': email,
            'list_id': list_id
        }
        return self.api_client.send_request('lists.last_status', params)

    def get_import_history(self, list_id: int = None):
        params = {
            "list_id": list_id
        }
        return self.api_client.send_request('lists.get_import_history', params)
        
    def check_email(self, email: str, list_id: int = None):
        params = {
            'email': email,
            'list_id': list_id
        }
        return self.api_client.send_request('lists.check_email', params)


    