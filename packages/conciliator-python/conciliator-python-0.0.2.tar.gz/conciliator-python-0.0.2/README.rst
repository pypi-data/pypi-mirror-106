conciliator-python
============
Python library for the Conciliator API


Introduction
------------
Python client library for Conciliator (https://expert.conciliator.ai/)

Installation
----------------
    >>> pip install conciliator-python

Usage
------------
```python
import conciliator as cc

cc.connect(username, pwd, tenant)
for entity in cc.Entity.list():
  print(entity.name)
  for f in cc.File.list(entity)
    print(f.name)
```
