import sys
import traceback

class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        super(CustomException, self).__init__(*args, **kwargs)

def custom_deep_function():
	raise CustomException('Test to raise custom exception.')

def custom_function():
	custom_deep_function()

try:
    custom_function()
except:
    _type, _value, _traceback = sys.exc_info()
    print(''.join(str(entry) for entry in traceback.format_tb(_traceback, limit=10)))
