class Init:
	def __init__(self):
		try:
			from tkinter import *
			from tkinter.ttk import *
			from threading import Thread
			import requests
			import zipfile
			import time
			import os
			import sys
			from urllib import *
			from PIL import *
			import base64, PIL, urllib
			import shutil
			import urllib.request as urllib2
			import pythoncom
		except ImportError:
			raise ImportException("missing/corrupted lib(s)")


class ImportException(Exception):
	pass

if __name__ == '__main__':
	Init()