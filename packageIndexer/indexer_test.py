#!/usr/bin/env python

import unittest
from pind.indexer import *


class TestIndexerMethods(unittest.TestCase):

    # Test Package object with empty members
    def test_PackageObjectWithEmptyValue(self):
        self.assertEqual(str(Package()), "Package name: None")
        self.assertEqual(str(Package()._name), "None")
        self.assertEqual(Package()._dependencies, [])

    # Test Package object with non-empty name
    def test_PackageObjectWithNonEmptyValue(self):
        pkg = Package("gitk")
        self.assertEqual(str(pkg), "Package name: gitk")
        self.assertEqual(pkg._name, "gitk")
        self.assertEqual(pkg._dependencies, [])

    # Test Package object with non-empty name and dependencies
    def test_PackageObjectWithNonEmptyValues(self):
        pkg = Package("gitk", [1, 2, 3])
        self.assertEqual(str(pkg), "Package name: gitk")
        self.assertEqual(pkg._name, "gitk")
        self.assertEqual(pkg._dependencies, [1, 2, 3])

    # Test PackageIndexer index method: pass
    def test_PackageIndexerIndexMethod1(self):
        pkgIndexer = PackageIndexer()
        pkg = Package("gitk")
        self.assertEqual(pkgIndexer.index(pkg), True)

    # Test PackageIndexer index method: failure since
    #   dependency is not indexed
    def test_PackageIndexerIndexMethod2(self):
        pkgIndexer = PackageIndexer()
        dependencyPkg = Package("bob")
        pkg = Package("altassian", [dependencyPkg])
        self.assertEqual(pkgIndexer.index(pkg), False)

    # Test PackageIndexer index method: pass since
    #   dependency is indexed
    def test_PackageIndexerIndexMethod3(self):
        pkgIndexer = PackageIndexer()
        dependencyPkg = Package("chris")
        self.assertEqual(pkgIndexer.index(dependencyPkg), True)

        pkg = Package("mike", [dependencyPkg])
        self.assertEqual(pkgIndexer.index(pkg), True)

    # Test PackageIndexer remove method: pass
    def test_PackageIndexerRemoveMethod(self):
        pkgIndexer = PackageIndexer()
        pkg = Package("nancy")
        self.assertEqual(pkgIndexer.remove(pkg), True)

    # Test PackageIndexer remove method: fail since
    #   dependent package is being removed
    def test_PackageIndexerRemoveMethod2(self):
        pkgIndexer = PackageIndexer()

        dependencyPkg = Package("chris")
        pkgIndexer.index(dependencyPkg)

        pkg = Package("mike", [dependencyPkg])
        pkgIndexer.index(pkg)

        self.assertEqual(pkgIndexer.remove(dependencyPkg), False)

    # Test PackageIndexer query method: pass
    def test_PackageIndexerQueryMethod(self):
        pkgIndexer = PackageIndexer()
        pkg = Package("mike")
        pkgIndexer.index(pkg)
        self.assertEqual(pkgIndexer.query(pkg._name), True)

    # Test PackageIndexer query method: fail
    def test_PackageIndexerQueryMethod2(self):
        pkgIndexer = PackageIndexer()
        self.assertEqual(pkgIndexer.query("dummy"), False)

if __name__ == "__main__":
    unittest.main()
