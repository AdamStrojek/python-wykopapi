import unittest
from requests import api
from tests.config import APP_KEY, APP_SECRET, USER_LOGIN, USER_KEY
from wykopapi import Wykop, WykopException

__author__ = 'astrojek'


class UserTest(unittest.TestCase):

    def setUp(self):
        self.api = Wykop(api_key=APP_KEY, api_secret=APP_SECRET)

    def tearDown(self):
        pass
        # self.api.logout()

    def testGood(self):
        result = self.api.login(USER_LOGIN, account_key=USER_KEY)

        self.assertIsNotNone(result, "Could not login")

    def testBad(self):
        with self.assertRaises(WykopException) as cm:
            self.api.login(USER_LOGIN, account_key="bad key")

        the_exception = cm.exception
        self.assertEqual(the_exception.code, 15, "Other exception then invalid login or password!")
