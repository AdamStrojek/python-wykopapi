import unittest

__author__ = 'astrojek'

from tests.config import KEYS, USER, USERKEY

from wykop import Wykop


class ConnectionTest(unittest.TestCase):

    def testConn(self):
        KEY, SECRET = KEYS['connection']

        api = Wykop(api_key=KEY, api_secret=SECRET)
        result = api.request(type=['user', 'login'], login=USER, accountkey=USERKEY)

        self.assertIsNotNone(result, "Not a userkey")