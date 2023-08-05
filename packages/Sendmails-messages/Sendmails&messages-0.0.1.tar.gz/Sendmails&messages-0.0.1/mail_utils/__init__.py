#  __init__.py file  is used to make imports more succinct. can leave blank also

#It allows you to treat a directory as if it was a python module. 

from .current_time import current_time

from .validate_mail import check_email

from .validate_number import check_mobileno

from .write_file import write_to

import getpass

sender_mail = input("Enter sender mail >> ")
password = getpass.getpass('Enter Password of sender and press Enter >> ')
