from setuptools import setup

setup(
    name='nmea-parser',
    version='0.1.0',
    packages=['nmea'],
    url='https://gitlab.com/bek3/nmea-parser',
    license='Mozilla Public License 2.0',
    author='Brendan Kristiansen',
    author_email='b@bek.sh',
    description='Python library to parse NMEA streams',
    install_requires=['pyserial']
)
