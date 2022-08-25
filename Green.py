import os, sys
try:
    __import__("green64").rhf()
except Exception as e:
    exit(str(e))
