#!/usr/bin/env python

import re
from ..indexer import Package, PackageIndexer


class RequestCommand():
    """This class wraps requested input message into an object.

    Attributes:
        _command (str): The command either of: INDEX, REMOVE, QUERY
        _package (Package): The package to run the @command one
    """

    def __init__(self,
                 command=None,
                 package=None):
        self._command = command
        self._package = package

    def __repr__(self):
        """Returns a string representation of RequestCommand object."""

        return "%s: %s" % (self._command, self._package)

    # __str__ is the same as __repr__
    __str__ = __repr__


def getRequestCommand(requestData):
    """This function creates RequestCommand object for incoming data.

    A valid @requestData has the format: `<command>|<package>|<dependencies>\n`.
    It returns an error if the input data is invalid.

    Args:
        requestData (str): The input request data from the client

    Returns:
        On successful parsing of @requestData, returns a RequestCommand object else None
    """

    if isinstance(requestData, (int, long)):
        return None

    requestDataPattern = '^(INDEX|REMOVE|QUERY){1}\|(.+){1}\|(.*)'
    match = re.search(requestDataPattern, requestData)

    if match is None:
        return None

    command = match.group(1)
    packageName = match.group(2)
    dependencies = match.group(3).split(",")

    package = Package(packageName)
    for depName in dependencies:
        if not depName:
            continue
        package._dependencies.append(Package(depName))

    requestCommand = RequestCommand(command, package)
    return requestCommand


def processRequestCommand(reqCommand, packIndexer):
    """This function processes the @reqCommand object.

    It also ensures a synchronized processing since the @packIndexer
    is a shared resource among all the threads

    Args:
        reqCommand (str): The input request command
        packIndexer (PackageIndexer): The PackageIndexer object

    Returns:
        A boolean value indicating success or failure for operations: index, remove, query
    """

    if not isinstance(reqCommand, (RequestCommand)) or not isinstance(packIndexer, (PackageIndexer)):
        return False

    packIndexer._lockObj.acquire()

    returnResult = True

    if reqCommand._command == "INDEX":
        returnResult = packIndexer.index(reqCommand._package)
    elif reqCommand._command == "REMOVE":
        returnResult = packIndexer.remove(reqCommand._package)
    elif reqCommand._command == "QUERY":
        returnResult = packIndexer.query(reqCommand._package._name)

    packIndexer._lockObj.release()

    return returnResult
