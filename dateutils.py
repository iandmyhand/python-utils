##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Dates.
"""
import datetime
import unittest

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015, Python Utils Project'

__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Development'


class TestDateUtils(unittest.TestCase):

    def test_is_valid_date(self):
        self.assertTrue(DateUtils().is_valid_date('20151021'))
        self.assertFalse(DateUtils().is_valid_date('20151041'))
        self.assertFalse(DateUtils().is_valid_date('2015102'))
        self.assertFalse(DateUtils().is_valid_date('20151000'))


class DateUtils:

    def is_valid_date(self, birthdate):
        """
            Usage:
                DateUtils().is_valid_date('20151021')  # True
                DateUtils().is_valid_date('20151041')  # False
        """
        if 8 != len(birthdate):
            return False

        if not birthdate.isdigit():
            return False

        try:
            datetime.datetime.strptime(birthdate, '%Y%m%d')
        except ValueError:
            return False

        return True

if __name__ == '__main__':
    unittest.main()
