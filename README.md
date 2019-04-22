# Python MapR Client
This repo hosts a Python module that implements bindings against the
libMapRClient.so binary.

This module does NOT implement every available API. This is merely a proof of
concept for accessing MapR binary tables with Python.

## Requirements

- Python 3

## Example Usage

Path to libjvm.so:
```
export LD_LIBRARY_PATH=/usr/lib/jvm/java-1.8.0-openjdk/jre/lib/amd64/server
```

If you are running secure mode:
```
export MAPR_TICKETFILE_LOCATION=/path.to/mapr-ticket
```

Modify ```table_name``` in main()``` before running:
```
python3 example/table_scan.py
```
