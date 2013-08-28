import unittest

__author__ = 'astrojek'

from tests.config import APP_KEY, APP_SECRET, USER_LOGIN, USER_KEY

from wykopapi import Wykop


class ConnectionTest(unittest.TestCase):

    def testConn(self):
        api = Wykop(api_key=APP_KEY, api_secret=APP_SECRET)
        result = api.request(resource=['user', 'login'], login=USER_LOGIN, accountkey=USER_KEY)

        self.assertIsNotNone(result, "Not a userkey")

