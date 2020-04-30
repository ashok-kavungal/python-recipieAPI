from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):
    """ test cases for helper commands to avoid django tries to connect ,before postgres is ready"""
    
    def test_wait_for_db_ready(self):
        """mocking condition where postgres is ready when django tries to connect"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True ##sets the connectionn handlerr return value to succesful
            call_command('wait_for_postgres')#custom command added in core
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """simulate conddition where postgres is not ready for the first 5 connect request"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True] ##returns error for first 5 times
            call_command('wait_for_postgres')
            self.assertEqual(gi.call_count, 6)