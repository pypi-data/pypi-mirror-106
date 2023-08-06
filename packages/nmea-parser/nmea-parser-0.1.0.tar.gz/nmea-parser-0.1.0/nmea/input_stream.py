""" Module containing a generic input stream
"""

from typing import Union
from pathlib import Path, PosixPath

import serial

__author__ = "Brendan Kristiansen"
__copyright__ = "Copyright 2021, Brendan Kristiansen"
__credits__ = ["Brendan Kristiansen"]
__license__ = "MPL 2.0"
__version__ = "0.1.0"
__maintainer__ = "Brendan Kristiansen"
__email__ = "b@bek.sh"


class GenericInputStream:
    """ Generic input stream
    """

    @staticmethod
    def open_stream(path: Union[str, Path], baud=4800):
        """ Input stream factory

        :param path: Path to stream (file or serial port)
        :param baud: Baud rate of serial port. Ignored if file

        :return: Input stream instance

        """

        if not isinstance(path, str) or not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")
        if not isinstance(baud, int):
            raise TypeError("Baud rate must be an integer")

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError("Specified GNSS source does not exist.")

        if path.is_char_device():
            return SerialPort(path, baud=baud)

        return InputFileStream(path)


    def get_line(self) -> bytes:
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class InputFileStream (GenericInputStream):
    """ Read GPS data from a file
    """

    _fp = None

    def __init__(self, path: Union[Path, str]):

        if not isinstance(path, str) or not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")

        self._fp = open(path, "rb")

    def get_line(self) -> bytes:

        return self._fp.readline()

    def close(self):

        self._fp.close()


class SerialPort (GenericInputStream):
    """ Read NMEA stream from a serial port
    """

    _port: serial.Serial

    def __init__(self, path: Union[str, Path], baud: int = 4800):

        if not isinstance(path, str) or not isinstance(path, Path):
            raise TypeError("Path must be a string or pathlib.Path")
        if not isinstance(baud, int):
            raise TypeError("Baud rate must be an integer")

        self._port = serial.Serial(port=path, baudrate=baud)

    def get_line(self) -> bytes:

        return self._port.readline()

    def close(self):

        self._port.close()
