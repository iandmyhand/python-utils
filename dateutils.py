##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Dates.
"""
import datetime
import unittest

from calendar import monthrange
from dateutil import relativedelta

from numberutils import NumberUtils

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015, Python Utils Project'

__license__ = 'MIT'
__version__ = '0.0.2'
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

    def test_get_age_band(self):
        today = datetime.datetime.today()
        year = today.year - 36
        self.assertEqual(30, DateUtils().get_age_band(year=year))
        year = today.year - 41
        self.assertEqual(40, DateUtils().get_age_band(year=year))
        year = today.year - 99
        self.assertEqual(90, DateUtils().get_age_band(year=year))

    def test_month_delta(self):
        date1 = datetime.datetime.strptime(str('2011-08-14 12:00:00'), '%Y-%m-%d %H:%M:%S')
        date2 = datetime.datetime.strptime(str('2012-02-15'), '%Y-%m-%d')
        self.assertEqual(6, DateUtils().month_delta(date1, date2))
        self.assertEqual(-6, DateUtils().month_delta(date2, date1))


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
            DateUtils().get_first_date_of_next_month()  # if today is 2016.2.24 then return datetime.date(2016, 3, 1)
            DateUtils().get_first_date_of_next_month(datetime.datetime(2016, 12, 31))  # datetime.date(2017, 1, 1)
        Args:
            base_date: datetime.date
        """
        if 12 < base_date.month + 1:
            return datetime.date(base_date.year + 1, 1, 1)
        else:
            return datetime.date(base_date.year, base_date.month + 1, 1)

    def get_age_band(self, year):
        """
        Usage:

        Args:
            year: four digit number or string.
        """
        return NumberUtils(datetime.datetime.today().year - int(year)).round_down(1)

    def month_delta(self, d1, d2):
        delta = 0
        while True:
            mdays = monthrange(d1.year, d1.month)[1]
            d1 += datetime.timedelta(days=mdays)
            if d1 <= d2:
                delta += 1
            else:
                break
        return delta


if __name__ == '__main__':
    unittest.main()
