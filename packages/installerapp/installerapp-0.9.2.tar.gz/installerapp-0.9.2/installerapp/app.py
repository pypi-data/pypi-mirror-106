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
from installerapp import namehandler

installed = False

class InstallerGUI(Frame):
	def __init__(self, root, to_dl):
		super().__init__()

		self.root = root

		icon = requests.get("https://findicons.com/icon/download/64181/folder_actions_setup/128/ico")
		b64_data = base64.encodebytes(icon.content)
		root.iconbitmap(False, b64_data)

		self.aliveThread = True
		self.state = False
		self.installed = False

		if to_dl != "":
			self.filename = namehandler.get_filename(to_dl)
			self.installer = Installer(to_dl, self, self.filename)
		else:
			raise FileURLException("empty URL")

		self.initUI()
		uiThread = Thread(target=self.threadUI)
		uiThread.start()

		self.to_dl = to_dl

	def initUI(self):
		self.master.title("InstallerApp")
		self.style = Style()

		self.pack(fill=BOTH, expand=True)

		self.waitingText = Label(self, text="Waiting to install...")
		self.waitingText.pack(pady=10)

		self.progressBar = Progressbar(self, orient=HORIZONTAL, length=250, mode="determinate")
		self.progressBar.pack(pady=5)

		self.installBtn = Button(self, text="Install", command=self.act)
		self.installBtn.pack(side=RIGHT, padx=5, pady=5)

	def act(self):
		if not self.state:
			self.state = True
		else:
			self.aliveThread = False
			sys.exit()

	def threadUI(self):
		while self.aliveThread:
			if self.state:
				if not self.installed:
					self.waitingText['text'] = "Installing..."

					self.installBtn['state'] = DISABLED

					self.installer.install()
					self.installed = True

					if namehandler.get_format(self.filename) == "zip":
						self.installer.unzip()
					else:
						self.installer.after_installed()
				else:
					pass
			else:
				pass
		else:
			sys.exit()


class Installer(object):
	def __init__(self, url, master, filename):
		self.url = url
		self.master = master

		self.sizeThread = Thread(target=self.getSize)

		self.filename = filename
		

	def install(self):
		u = urllib2.urlopen(self.url)
		f = open(self.filename, 'wb')
		file_size = int(u.getheader('Content-Length'))
		file_size_dl = 0
		block_sz = 8192

		while True:
		    buffer = u.read(block_sz)
		    if not buffer:
		        break

		    file_size_dl += len(buffer)
		    f.write(buffer)
		    self.master.progressBar['value'] = file_size_dl * 100. / file_size
		    self.master.waitingText['text'] = "Installing " + str(round(file_size_dl/1048576, 1)) + " / " + str(round(file_size/1048576, 1)) + " MB ..."

		f.close()

	def unzip(self):
		try:
			with zipfile.ZipFile(self.filename, 'r') as zip_ref:
			    zip_ref.extractall(namehandler.get_filename_without_format(self.filename))
			    zip_ref.close()

			    self.master.waitingText['text'] = "Extracting..."

			    for i in range(76):
			    	self.master.progressBar['value'] = 0 + i
			    	time.sleep(0.001)

			    self.rmvFiles()

		except zipfile.BadZipfile:
			time.sleep(0.5)
			self.unzip()

	def rmvFiles(self):
		os.remove(self.filename)

		for i in range(26):
			self.master.progressBar['value'] = 75 + i
			time.sleep(0.01)

		self.after_installed()

	def after_installed(self):
		self.master.waitingText['text'] = "Installed " + self.filename + " with 0 errors"

		self.master.installBtn['state'] = NORMAL
		self.master.installBtn['text'] = "Quit"

	def getSize(self):
		response = urllib2.urlopen(self.url)
		headers = response.getheaders()
		file_size = int(response.getheader('Content-Length'))
		megaBytes = round(file_size/1048576, 1)

		self.master.waitingText['text'] = "Installing " + str(megaBytes) + " MB ..."


class InstallerApp(object):
	global to_dl

	def __init__(self, file_to_dl: str):
		self.to_dl = file_to_dl

	def run(self):
		root = Tk()
		root.geometry("300x110")

		app = InstallerGUI(root, self.to_dl)
		root.mainloop()

	def run_installer(self):
		self.run()


class FileURLException(Exception):
	sys.exit(1)
	pass
