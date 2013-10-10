import unittest
import hashlib
from tests.config import APP_KEY, APP_SECRET
from wykopapi.utils import build_api_params, build_post_params, sign_post_params

__author__ = 'astrojek'


class ParamsTest(unittest.TestCase):

    def build_api_params_string_test(self):
        api_params = {
            'appkey': 'my_app_key',
            'page': '1',
        }

        result = build_api_params(api_params)

        self.assertEqual(result, 'appkey,my_app_key,page,1', "API Params don't match!")

    def checksum_test(self):
        URL = "https://a.wykop.pl/foo/bar/index/page,1"
        DATA_A = "foo"
        DATA_B = "4"
        DATA_C = "BAR"
        DATA_D = "WYKOP"
        DATA_K = "!!!!"
        post_data = dict(
            a=DATA_A,
            k=DATA_K,
            d=DATA_D,
            b=DATA_B,
            c=DATA_C
        )

        """
            From Wykop API documentation:

            Requests are signed by MD5 sum of application secret, request URL and post params values sorted by keys.
        """
        md = hashlib.new('md5')
        md.update(APP_SECRET)
        md.update(URL)
        md.update(DATA_A)
        md.update(DATA_B)
        md.update(DATA_C)
        md.update(DATA_D)
        md.update(DATA_K)

        result1 = md.hexdigest()
        result2 = sign_post_params(APP_SECRET, URL, post_data)

        self.assertEqual(result1, result2, "MD5 sums don't match!")
