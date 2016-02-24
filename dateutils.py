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

    def test_get_first_date_of_next_month(self):
        base_date = datetime.datetime(2016, 12, 31)
        next_month = DateUtils().get_first_date_of_next_month(base_date=base_date)
        self.assertEqual(1, next_month.month)
        base_date = datetime.datetime(2016, 1, 1)
        next_month = DateUtils().get_first_date_of_next_month(base_date=base_date)
        self.assertEqual(2, next_month.month)


class DateUtils:

    def is_valid_date(self, birth_date):
        """
        Usage:
            DateUtils().is_valid_date('20151021')  # True
            DateUtils().is_valid_date('20151041')  # False
        Args:
            birth_date:

        Returns:

        """
        
        if 8 != len(birth_date):
            return False

        if not birth_date.isdigit():
            return False

        try:
            datetime.datetime.strptime(birth_date, '%Y%m%d')
        except ValueError:
            return False

        return True

    def get_first_date_of_next_month(self, base_date=datetime.datetime.today()):
        """
        Usage:
            DateUtils().get_first_date_of_next_month() # if today is 2016.2.24 then return datetime.date(2016, 3, 1)
            DateUtils().get_first_date_of_next_month(datetime.datetime(2016, 12, 31))  # datetime.date(2017, 1, 1)
        Args:
            base_date: datetime.date
        """
        if 12 < base_date.month + 1:
            return datetime.date(base_date.year + 1, 1, 1)
        else:
            return datetime.date(base_date.year, base_date.month + 1, 1)


if __name__ == '__main__':
    unittest.main()
