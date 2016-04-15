import sys
import traceback

class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        super(CustomException, self).__init__(*args, **kwargs)

def custom_function():
	raise CustomException('Test to raise custom exception.')

try:
    custom_function()
except:
    _type, _value, _traceback = sys.exc_info()
    for _entry in traceback.format_tb(_traceback):
    	print(_entry)
