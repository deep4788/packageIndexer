#!/usr/bin/env python

import threading


class Package():
    """This class represents a package.

    Attributes:
        _name (str): The name of the package
        _dependencies (list): The list of packages that this package dependents on
    """

    def __init__(self,
                 name=None,
                 dependencies=None):
        self._name = name
        if dependencies is None:
            self._dependencies = []
        else:
            self._dependencies = dependencies

    def __repr__(self):
        """Returns a string representation of Package object."""

        return "Package name: %s" % (self._name)

    # __str__ is the same as __repr__
    __str__ = __repr__


class PackageIndexer():
    """This class represents a package indexer.

    A package can be either: indexed, removed, queried.

    Attributes:
        _packageIndexer (str): A dictionary that keeps track of packages indexing
        _lockObj (threading.Lock): A lock object that synchronizes operations on shared resource
    """

    def __init__(self):
        self._packageIndexer = {}  # key = Package Name, value = Package
        self._lockObj = threading.Lock()  # Lock object

    def index(self, package):
        """This function indexes a package.

        If the package is already indexed, it updates its dependencies.
        If any of package's dependencies are unknown, it returns an error.

        Args:
            package (Package): A Package object to be indexed

        Returns:
            A boolean indicating whether the package was successfully indexed or not
        """

        # Iterate over all the dependencies of @package
        #   to see if they are indexed or not
        for depenPackage in package._dependencies:
            if not self.query(depenPackage._name):
                return False

        self._packageIndexer[package._name] = package
        return True

    def remove(self, package):
        """This function removes a package.

        If no other package depends on this package, it removes this package.
        If any other package depends on it, it returns an error.

        Args:
            package (Package): A Package object to be removed

        Returns:
            A boolean indicating whether the package removal was successful or not
        """

        for _, pkg in self._packageIndexer.iteritems():
            for depenPackage in pkg._dependencies:
                if package._name == depenPackage._name:
                    return False

        try:
            del self._packageIndexer[package._name]
        except KeyError:
            pass

        return True

    def query(self, packageName):
        """This function searches index for a package.

        Args:
            packageName (str): The package name to be searched.

        Returns:
            A boolean indicating whether the package is indexed or not
        """

        if packageName in self._packageIndexer:
            return True
        else:
            return False
