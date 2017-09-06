#!/usr/bin/env python

import unittest
from pind.handleRequest import *
from pind.indexer import *


class TestHandleRequestMethods(unittest.TestCase):

    # Test RequestCommand object with empty members
    def test_RequestCommandObjectEmptyValues(self):
        self.assertEqual(str(RequestCommand()), "None: None")

    # Test RequestCommand object with non-empty command member
    def test_RequestCommandObjectNonEmptyCommand(self):
        self.assertEqual(str(RequestCommand("INDEX")), "INDEX: None")

    # Test RequestCommand object with members:
    #   command non-empty and package name empty
    def test_RequestCommandObjectMixedValues(self):
        pkg = Package()
        self.assertEqual(str(RequestCommand("INDEX", pkg)), "INDEX: Package name: None")

    # Test RequestCommand object with members:
    #   command non-empty and package name non-empty
    def test_RequestCommandObjectMixedValues2(self):
        pkg = Package("gitk")
        self.assertEqual(str(RequestCommand("INDEX", pkg)), "INDEX: Package name: gitk")

    # Test RequestCommand object with members:
    #   command empty and package name non-empty
    def test_RequestCommandObjectMixedValues3(self):
        pkg = Package("gitk")
        self.assertEqual(str(RequestCommand(None, pkg)), "None: Package name: gitk")

    # Test getRequestCommand() function with empty argument
    def test_getRequestCommandEmptyArg(self):
        self.assertEqual(getRequestCommand(""), None)

    # Test getRequestCommand() function with int argument
    def test_getRequestCommandIntArg(self):
        self.assertEqual(getRequestCommand(2), None)

    # Test getRequestCommand() function with incorrect string
    def test_getRequestCommandIncorrectString(self):
        self.assertEqual(getRequestCommand("hi"), None)

    # Test getRequestCommand() function with incorrect string
    def test_getRequestCommandIncorrectString2(self):
        self.assertEqual(str(getRequestCommand("INDEX||gmp,bob\n")), "None")

    # Test getRequestCommand() function with incorrect string
    def test_getRequestCommandIncorrectString3(self):
        self.assertEqual(str(getRequestCommand("|cloog|gmp,bob\n")), "None")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString1(self):
        self.assertEqual(str(getRequestCommand("INDEX|cloog|gmp\n")), "INDEX: Package name: cloog")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString2(self):
        self.assertEqual(str(getRequestCommand("REMOVE|cloog|\n")), "REMOVE: Package name: cloog")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString3(self):
        self.assertEqual(str(getRequestCommand("QUERY|cloog|\n")), "QUERY: Package name: cloog")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString4(self):
        self.assertEqual(str(getRequestCommand("INDEX|cloog|gmp,bob\n")), "INDEX: Package name: cloog")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString5(self):
        self.assertEqual(str(getRequestCommand("INDEX|cloog|\n")), "INDEX: Package name: cloog")

    # Test getRequestCommand() function with correct string
    def test_getRequestCommandCorrectString6(self):
        self.assertEqual(str(getRequestCommand("INDEX|cloog|")), "INDEX: Package name: cloog")

    # Test processRequestCommand() function with empty arguments
    def test_processRequestCommandWithEmptyArgs(self):
        self.assertEqual(str(processRequestCommand("", "")), "False")

    # Test processRequestCommand() function with good arguments
    def test_processRequestCommandWithGoodArgs(self):
        pkgIndexer = PackageIndexer()
        reqCommand = RequestCommand("INDEX", Package("gitk"))
        self.assertEqual(str(processRequestCommand(reqCommand, pkgIndexer)), "True")

    # Test processRequestCommand() function with wrong RequestCommand type
    def test_processRequestCommandWithWrongArgType1(self):
        pkgIndexer = PackageIndexer()
        self.assertEqual(str(processRequestCommand("", pkgIndexer)), "False")

    # Test processRequestCommand() function with wrong RequestCommand type
    def test_processRequestCommandWithWrongArgType2(self):
        reqCommand = RequestCommand("INDEX", Package("gitk"))
        self.assertEqual(str(processRequestCommand(reqCommand, "")), "False")

if __name__ == "__main__":
    unittest.main()
