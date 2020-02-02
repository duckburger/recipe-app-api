from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        '''Test waiting for db when it is available'''
        # This is what django calls in the source code to retrieve a database
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            # Counts how many times this mock function has been called
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        '''Test waiting for db'''
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Raise error 5 times then return on the 6th
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
