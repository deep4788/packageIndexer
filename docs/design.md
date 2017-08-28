## Package Indexer

*Packages* are executables or libraries that can be installed in a system, often via a package manager such as RPM or Homebrew. Many packages use libraries that are also made available as packages themselves, so usually a package will require us to install its dependencies before we can install it on our system.

This system (server) keeps track of package dependencies. Clients will connect to this server and inform it about which packages should be indexed, and which dependencies they might have on other packages. The server keeps the index consistent, i.e. it does not index any package until all of its dependencies have been indexed first. The server also does not remove a package if any the other packages depend on it.

The server opens a TCP socket on port 8080. It accepts connections from multiple clients at the same time, all trying to add and remove items to the index concurrently. Clients are independent of each other, and they can send repeated or contradicting messages.

Messages from clients follow this pattern:

```
<command>|<package>|<dependencies>\n
```

Where:

* `<command>` is mandatory, and is either `INDEX`, `REMOVE`, or `QUERY`
* `<package>` is mandatory, the name of the package referred to by the command, e.g. `mysql`, `openssl`, `pkg-config`, `postgresql`, etc.
* `<dependencies>` is optional, and if present it will be a comma-delimited list of packages that need to be present before `<package>` is installed. e.g. `cmake,sphinx-doc,xz`
* The message always ends with the character `\n`

Here are some sample messages:

```
INDEX|dummy|gimp,dep2,pkg-config\n
INDEX|pkg2|\n
REMOVE|dummy|\n
QUERY|dummy|\n
```

For each message sent, the client will wait for a response code from the server. Possible response codes are `OK\n`, `FAIL\n`, or `ERROR\n`. After receiving the response code, the client can send more messages.

The response code returned should be as follows:

- For `INDEX` commands, the server returns `OK\n` if the package can be indexed. It returns `FAIL\n` if the package cannot be indexed because some of its dependencies aren't indexed yet and need to be installed first. If a package already exists, then its list of dependencies is updated to the one provided with the latest command.
- For `REMOVE` commands, the server returns `OK\n` if the package could be removed from the index. It returns `FAIL\n` if the package could not be removed from the index because some other indexed package depends on it. It returns `OK\n` if the package wasn't indexed.
- For `QUERY` commands, the server returns `OK\n` if the package is indexed. It returns `FAIL\n` if the package isn't indexed.
- If the server doesn't recognize the command or if there's any problem with the message sent by the client it should return `ERROR\n`.
