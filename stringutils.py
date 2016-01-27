##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to String.
"""

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015 SeomGi, Han, Python Utils Project'

__license__ = 'MIT'
__version__ = '1.0.1'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Production'


class NotSupportedException(Exception):

    def __init__(self, message, errors):
        super(NotSupportedException, self).__init__(message)
        self.errors = errors


class StringUtils:

    _string_value = ''
    _len_string_value = 0

    def __init__(self, string_value=''):
        self._string_value = str(string_value)
        self._len_string_value = len(self._string_value)

    def __del__(self):
        self._string_value = ''
        self._len_string_value = 0

    def extract_file_name(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_file_name() returns 'filename.py'
        """
        result = ''
        if self._string_value:
            arr = self._string_value.split('/')
            result += arr[len(arr) - 1]

        return result

    def extract_extension(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_extension() returns 'py'
        """
        arr = self._string_value.split('.')
        extension = arr[len(arr) - 1]
        return extension

    def extract_directory(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_extension() returns '/path/to/'
        """
        return self._string_value[:self._string_value.rfind('/') + 1]

    def get_content_type(self):
        """
        usage:
            StringUtils('filename.png').get_content_type() returns 'image/png'
        """
        extension = self.extract_extension()
        if 'png' == extension:
            return 'image/png'
        elif 'jpg' == extension:
            return 'image/jpg'
        elif 'jpeg' == extension:
            return 'image/jpeg'
        elif 'gif' == extension:
            return 'image/gif'
        elif 'bmp' == extension:
            return 'image/bmp'
        elif 'tif' == extension or 'tiff' == extension:
            return 'image/tiff'
        elif 'pdf' == extension:
            return 'application/pdf'
        elif 'zip' == extension:
            return 'application/zip'

        raise NotSupportedException(
            message='This extension[' + str(extension) + '] is not supported.',
            errors={'code': 'NOT_SUPPORTED_EXTENSION'})
