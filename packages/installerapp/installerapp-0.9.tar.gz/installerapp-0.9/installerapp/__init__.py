class Init:
	def __init__(self):
		try:
			import tkinter
			import threading
			import requests
			import zipfile
			import time
			import os
			import sys
			import base64, PIL, urllib
			import shutil
			import pythoncom
		except ImportError:
			raise ImportException("missing/corrupted lib(s)")


class ImportException(Exception):
	pass

if __name__ == '__main__':
	Init()