import unittest

from dasha_mail import dasha_api_client
from dasha_mail import configuration


class TestConfiguration(unittest.TestCase):

    def setUp(self) -> None:
        self.api_client = dasha_api_client.DashaApiClient()
        configuration.Configuration.configure("047dc2e62b1694e88aeca1da2dc87837")

    def test_configured(self):
        data = self.api_client.send_request('lists.get')
        print(data)
