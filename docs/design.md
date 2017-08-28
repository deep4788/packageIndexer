# Design of Package Indexer

This document covers the design rationale of Package Indexer (PI) implementation. The PI is divided into three components as described below. Each component handles one specific task and together they provide PI's functionality.

## Components

Package Indexer is made up of various components:

- Server (multi-threaded)
- Request Handler
- Indexer

### Server

This component handles the TCP server, a multi-threaded server that listens for in-coming clients and lauches separate thread for each client. The thread function handles the parsing of the request data and processes it and then returns the response back to the client. It uses request handler and indexer components for these tasks.

### Request Handler

This component provides functionality to handle the client's request. It provides parsing of client's request data, creating meaningful command object from it and also provides function to process the request. It does it by taking the client's command and calling appropriate method (index, remove, query) on the PackageIndexer object.

Each client thread uses this handler to process the client request.

### Indexer

This component handles the main indexing feature. It provides Package and PackageIndexer classes. The Package class provides an object representation of a package.

The PackageIndexer class handles keeping track of the packages indexes and provides the three main functions that can be run on a given package: index, remove, query.
