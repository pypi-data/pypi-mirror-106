from setuptools import setup, find_packages
import os


VERSION = '0.0.1'
DESCRIPTION = 'scheduling mails and messages'
LONG_DESCRIPTION = 'A package that allows to take data like message,mobileno, email and scheduleon from csv file and send mails,text messages.'

# Setting up
setup(
    name="Sendmails&messages",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<peddintigokul946@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['schedule', 'twilio'],
    keywords=['python', 'twilio','schedule','smtp','send_mail','send_text'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)