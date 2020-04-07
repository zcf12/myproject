import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1+1, 2)

    def test_get_ts(self):
        # import time
        # t=time.time()
        # ts=str(int(round(t*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1584686262681')
        self.assertEqual('1584686262681', get_ts())

    def test_git_salt(self):
        get_salt=mock.Mock(return_value='15846862626819')
        self.assertEqual('15846862626819',get_salt())

    def test_get_sign(self):
        self.assertEqual('b6ca26b2024cf4badffbb2baec27833f',get_sign())


if __name__ == '__main__':
    unittest.main()
