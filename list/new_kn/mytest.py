from myPY import CheckUserInfo
import unittest


class CheckUserInfoTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.check_user_info = CheckUserInfo()

    @classmethod
    def setUpClass(cls):
        print('setUpClass\n\n')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown\n')

    def test_check_pwd_len(self):
        print('test_check_pwd_len')
        self.assertEqual(True, self.check_user_info.check_pwd_len('12345678'))
        self.assertEqual(False, self.check_user_info.check_pwd_len(''))
        self.assertEqual(False, self.check_user_info.check_pwd_len('1'))
        self.assertEqual(True, self.check_user_info.check_pwd_len('123456789'))

    def test_check_pwd_contain_letter(self):
        print('test_check_pwd_contain_leter')
        self.assertEqual(True, self.check_user_info.check_pwd_contain_leter('1qazXSW@'))
        self.assertEqual(False, self.check_user_info.check_pwd_contain_leter('12345678'))
        self.assertEqual(False, self.check_user_info.check_pwd_contain_leter(''))

    def aaa(self):
        print('test_check_pwd_contain_num')
        self.assertEqual(True, self.check_user_info.check_pwd_contain_num('1qazXSW@'))


if __name__ == '__main__':
    unittest.main()
"""
setUpClass
setUp
test_check_pwd_contain_leter
tearDown
FsetUp
test_check_pwd_len
tearDown
.tearDownClass
======================================================================
FAIL: test_check_pwd_contain_letter (__main__.CheckUserInfoTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "mytest.py", line 33, in test_check_pwd_contain_letter
    self.assertEqual(True, self.check_user_info.check_pwd_contain_leter('1qazXSW@'))
AssertionError: True != False
----------------------------------------------------------------------
Ran 2 tests in 0.001s
FAILED (failures=1)
"""
