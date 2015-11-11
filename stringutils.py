##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to String.
"""

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015 SeomGi, Han, Python Utils Project'

__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Production'


class StringUtils:

    _string_value = ''
    _len_string_value = 0

    def __init__(self, string_value=''):
        self._string_value = str(string_value)
        self._len_string_value = len(self._string_value)

    def __del__(self):
        self._string_value = ''
        self._len_string_value = 0

    def extract_file_name_from_path(self):
        """
        usage:
            stringutils.StringUtils('/path/to/filename.py').extract_file_name_from_path() returns 'filename.py'
        """

        result = ''
        if self._string_value:
            file_full_path_arr = self._string_value.split('/')
            result += file_full_path_arr[len(file_full_path_arr) - 1]

        return result
