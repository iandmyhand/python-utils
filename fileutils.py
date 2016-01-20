##-*- coding: utf-8 -*-
#!/usr/bin/python
"""
Utilities related to Files.
"""
from io import FileIO, BufferedWriter

__author__ = 'SeomGi, Han'
__credits__ = ['SeomGi, Han']
__copyright__ = 'Copyright 2015, Python Utils Project'

__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'SeomGi, Han'
__email__ = 'iandmyhand@gmail.com'
__status__ = 'Production'


class FileUtils:

    def copy_buffered_io_to_file(self, buffered_io, file_path):
        with FileIO(file_path, mode='wb') as raw_output_io:
            with BufferedWriter(raw_output_io) as writer:
                while 1:
                    line = buffered_io.readline()
                    if not line:
                        break
                    writer.write(line)
        buffered_io.close()
