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

    def test_get_timestamp_diff_formatted(self):
        _now = datetime.datetime.now()
        _date_utils = DateUtils()
        self.assertEqual('-', _date_utils.get_timestamp_diff_formatted(_now.timestamp(), _now.timestamp()))


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

    def get_timestamp_diff_formatted(self, big_timestamp, small_timestamp):
        if big_timestamp and isinstance(big_timestamp, int):
            _big_date = datetime.datetime.fromtimestamp(big_timestamp)
        else:
            _big_date = datetime.datetime.now()
        if small_timestamp and isinstance(small_timestamp, int):
            _small_date = datetime.datetime.fromtimestamp(small_timestamp)
        else:
            _small_date = datetime.datetime.now()

        return self.get_datetime_diff_formatted(_big_date, _small_date)

    def get_datetime_diff_formatted(self, big_date, small_date):
        if big_date and isinstance(big_date, datetime.datetime):
            _big_date = big_date
        else:
            _big_date = datetime.datetime.now()
        if small_date and isinstance(small_date, datetime.datetime):
            _small_date = small_date
        else:
            _small_date = datetime.datetime.now()

        if _big_date <= _small_date:
            return '-'

        _delta = _big_date - _small_date
        _remain_seconds = _delta.total_seconds()
        _remain_days = _remain_seconds // (24 * 60 * 60)
        _remain_seconds %= (24 * 60 * 60)
        _remain_hours = _remain_seconds // (60 * 60)
        _remain_seconds %= (60 * 60)
        _remain_minutes = _remain_seconds // 60
        if _remain_days:
            if _remain_hours:
                _result = '%d일 %d시간' % (_remain_days, _remain_hours)
            else:
                _result = '%d일 %d분' % (_remain_days, _remain_minutes if _remain_minutes else 1)
        elif _remain_hours:
            _result = '%d시간 %d분' % (_remain_hours, _remain_minutes if _remain_minutes else 1)
        elif _remain_minutes:
            _result = '%d분' % _remain_minutes
        else:
            _result = '1분 미만'

        return _result


if __name__ == '__main__':
    unittest.main()
