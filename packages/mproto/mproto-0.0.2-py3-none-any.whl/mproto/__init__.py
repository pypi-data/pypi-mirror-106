'''
Python library for managing custom protocols
Let Python make requests to urls such as "python://abc"
https://dev.to/pybash/making-a-custom-protocol-handler-and-uri-scheme-part-1-37mh
'''

from .proto import BaseProtoHandler

def install(*a):
  for i in a:
    getattr(i,'install')()