from dasha_mail.base_entity import BaseEntity


class Campaigns(BaseEntity):

    name = 'campaign'
    plural_name = 'campaigns'

    def create(self, list_id: int = None, **params):
        params.update({'list_id': list_id})
        return self.api_client.send_request('campaigns.create', params)

    def create_auto(self, list_id: int = None, **params):
        if list_id:
            params.update({'list_id': list_id})
        return self.api_client.send_request('campaigns.create_auto', params)

    def update(self, campaign_id: int = None, **params):
        params.update({'campaign_id': campaign_id})
        return self.api_client.send_request('campaigns.update', params)

    def update_auto(self, campaign_id: int = None, **params):
        params.update({'campaign_id': campaign_id})
        return self.api_client.send_request('campaigns.update_auto', params)

    def delete(self, campaign_id: int = None):
        return self.api_client.send_request(
                                                'campaigns.delete',
                                                {'campaign_id': campaign_id}
                                        )

    def attach(self, campaign_id: int = None, url: str = None, **params):
        params.update({'campaign_id': campaign_id, 'url': url})
        return self.api_client.send_request('campaigns.attach', params)

    def get_attachments(self, campaign_id: int = None):
        return self.api_client.send_request(
                                                'campaigns.get_attachments',
                                                {'campaign_id': campaign_id}
                                        )

    def delete_attachments(self, campaign_id: int = None, id: int = None):
        params = {'campaign_id': campaign_id, 'id': id}
        return self.api_client.send_request(
                                                'campaigns.delete_attachment',
                                                params
                                        )

    def get_templates(self, **params):
        return self.api_client.send_request('campaigns.get_templates', params)

    def get_saved_templates(self, **params):
        return self.api_client.send_request(
                                            'campaigns.get_saved_templates',
                                            params
                                        )

    def add_template(self, name: str = None, template: str = None):
        params = {'name': name, 'template': template}
        return self.api_client.send_request('campaigns.add_template', params)

    def delete_template(self, id: int = None):
        return self.api_client.send_request(
                                                'campaigns.delete_template',
                                                {'id': id}
                                        )

    def force_auto(
                self,
                campaign_id: int = None,
                member_id: int = None,
                **params):
        params.update({'campaign_id': campaign_id, 'member_id': member_id})
        return self.api_client.send_request('campaigns.force_auto', params)

    def multi_create(self, json: dict = None):
        return self.api_client.send_request(
                                        'campaigns.multi_create',
                                        {'json': json}
                                )

    def multi_get(self, campaign_id):
        return self.api_client.send_request(
                                                'campaigns.multi_get',
                                                {'campaign_id': campaign_id}
                                        )

    def multi_update(self, campaign_id: int = None, json: dict = None):
        return self.api_client.send_request(
                                                'campaign.multi_update',
                                                {
                                                    'campaign_id': campaign_id,
                                                    'json': json
                                                }
                                        )

    def get_folder(self, name: str = None, id: int = None):
        params = {'name': name, 'id': id}
        return self.api_client.send_request('campaigns.get_folder', params)

    def move_to_folder(self, campaign_id: int = None, folder_id: int = None):
        params = {'campaign_id': campaign_id, 'folder_id': folder_id}
        return self.api_client.send_request('campaigns.move_to_folder', params)

    def pause(self, campaign_id):
        return self.api_client.send_request(
                                                'campaigns.pause',
                                                {'campaign_id': campaign_id}
                                        )

    def restart_paused(self, campaign_id):
        return self.api_client.send_request(
                                                'campaigns.restart_paused',
                                                {'campaign_id': campaign_id}
                                        )
