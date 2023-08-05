import re
from .write_file import write_to

def check_email(email):

	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}[.]*[a-zA-Z]*$' 

	if(re.fullmatch(regex,email)):  
		write_to('messages.txt', 'a','Success : Email is valid..')
		return True  
	else:
		write_to('messages.txt', 'a',f'Failure : {email} Email is not valid..')
		return False