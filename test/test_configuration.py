import os
import unittest

from dasha_mail import dasha_api_client
from dasha_mail import configuration


class TestConfiguration(unittest.TestCase):

    def setUp(self) -> None:
        self.api_client = dasha_api_client.DashaApiClient()
        configuration.Configuration.configure(os.getenv("DASHA_API_TOKEN"))

    def test_configured(self):
        data = self.api_client.send_request('lists.get')
