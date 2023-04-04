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

########################################################################
    
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

############################################################################  

def reports_sent(self, campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.sent', params)

def reports_delivered(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.delivered', params)

def reports_opened(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.opened', params)

def reports_clicked(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.clicked', params)

def reports_unsubscribed(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.unsubscribed', params)

def reports_bounced(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.bounced', params)

def reports_codes(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.codes', params)

def reports_clickstart(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.clickstart', params)

def reports_userclicks(self,campaign_id:int=None, url:str=None, **params):
    params.update({'campaign_id':campaign_id, 'url':url})
    self.__send_request('reports.userclicks', params)

def reports_bouncestat(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.boucestat', params)

def reports_summary(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.summary', params)

def reporst_clients(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.clients', params)

def reports_geo(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.geo', params)

def reports_events(self,campaign_id:int=None, **params):
    params.update({'campaign_id':campaign_id})
    self.__send_request('reports.events', params)    

############################################################################  
def account_get_balance(self):
    self.__send_request('account.get_balance')

def account_get_webhooks(self,  **params):
    self.__send_request('account.get_webhooks', params)

def account_add_webhooks(self, **params):
    self.__send_request('account.add_webhooks', params)

def account_delete_webhooks(self, **params):
    self.__send_request('account.delete_webhooks', params)

def account_confirm_from_email(self, email:str=None,**params):
    params.update({'email':email})
    self.__send_request('account.confirm_from_email', params)

def account_get_confirmed(self):
    self.__send_request('account.get_confirmed')

def account_add_domain(self, **params):
    self.__send_request('account.add_domain', params)

def account_check_domains(self, **params):
    self.__send_request('account.check_domains', params)

def account_delete_domain(self, **params):
    self.__send_request('account.delete_domains', params)   