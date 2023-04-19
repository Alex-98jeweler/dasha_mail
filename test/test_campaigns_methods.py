from unittest import TestCase

from dasha_mail import Campaigns


class TestCampaignCreate(TestCase):

    def setUp(self) -> None:
        pass

    def test_create(self):
        """
        Тестируем метод создания  компании
        """
        pass
    
    def test_create_without_required_parameters(self):
        """
        Тестирование без указания обязательных параметров, проверяем всплывает ли исключение DashaMailException
        """
    
    def tearDown(self) -> None:
        pass
