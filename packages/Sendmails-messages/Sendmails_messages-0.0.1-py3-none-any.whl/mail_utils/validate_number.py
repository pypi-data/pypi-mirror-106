import re
from .write_file import write_to


def check_mobileno(mobile_number):
	match = re.fullmatch('[\d]{10}', mobile_number)
	if match!=None:
		write_to('messages.txt', 'a','Success : mobile number is correct')
	else:
		write_to('messages.txt', 'a',f'Failure :  Mobile number {mobile_number} not have 10 digits..')