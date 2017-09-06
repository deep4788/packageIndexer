#!/usr/bin/env python

import socket
import sys
import threading
import time

from . import __version__
from handleRequest import *
from indexer import *


class ThreadedServer(object):
    """This class represents the package indexer server.

    It creates a new thread for each newly accepted client.

    Attributes:
        _host (str): The address to launch server on
        _port (int): The port to launch server on
        _sock (socket.socket): The socket with socket type and protocol number
    """

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self._host, self._port))

    def listen(self):
        """This function listens for incoming connections.

        It used 100 for the backlog for maximum number of queued connections.
        """

        # TODO


    def handleConnection(self, client, address, packIndexer):
        """This function handles the connection for each client.

        It runs in a separate thread for each client.
        It is a callable object that is invoked by the run() method of threading.
        """

        # TODO


# Usage text
usage = """\
usage: pind [-h | -help]
            [port-number]

Example usage:
    pind        # Uses 8080 as the default port
    pind 7898   # Uses 7898 as the port number
    pind -h     # Prints help message
"""


def main():
    # Get command line arguments
    commandLineArgs = sys.argv
    argc = len(commandLineArgs)
    argv = commandLineArgs

    # Check if the script is ran with more than 2 arguments
    if(argc > 2):
        print usage
        sys.exit()

    host = ''
    port = 8080
    if(argc == 2):
        # If help command is passed, print usage and quit
        if(argv[1] == "-h" or argv[1] == "-help" or argv[1] == "h" or argv[1] == "help"):
            print usage
            sys.exit()

        # Check if port is provided
        port = commandLineArgs[1]
        try:
            port = int(port)
        except ValueError:
            port = 8080

    ThreadedServer(host, port).listen()

if __name__ == "__main__":
    main()
