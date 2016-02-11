##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Korean.
If you want to test this util, run in the terminal below code.
    $ python3 koreanutils.py
"""
import unittest

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015 SeomGi, Han, Python Utils Project'

__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Development'


class TestKoreanUtils(unittest.TestCase):

    def test_is_valid_korean_ssn(self):
        self.assertFalse(KoreanUtils().is_valid_korean_ssn('1234561234567'))


class KoreanUtils:

    def is_valid_korean_ssn(self, ssn):
        """
        usage:
            KoreanUtils().is_valid_korean_ssn('1234561234567') returns false
        """
        if 13 != len(ssn):
            return False

        return True


if __name__ == '__main__':
    unittest.main()
