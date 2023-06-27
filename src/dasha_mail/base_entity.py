from dasha_mail.dasha_api_client import DashaApiClient


class BaseEntity(object):

    name: str
    plural_name: str
    api_client = DashaApiClient()

    def get(self):
        return self.api_client.send_request(f'{self.plural_name}.get')

    def update(self, id, **params):
        params.update({f'{self.name}_id': id})
        return self.api_client.send_request(f'{self.plural_name}.update', params)

    def delete(self, id, **params):
        params.update({f'{self.name}_id': id})
        return self.api_client.send_request(
                                            f"{self.plural_name}.delete",
                                            params
                                        )
