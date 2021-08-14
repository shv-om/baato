"""
Python code file for Server Side executables!
File(s) will be shared from here
"""

import os
import json
import socket
import time

# Defining some Global Variables
CHUNK = 1024

class socket_server:

	def __init__(self):

		# Defining Hostname and Port
		self.host = input("Specify host's URL or IP-Address (just press enter to use default): ")
		if self.host is None:
			self.host = '0.0.0.0'
		
		# Creating Socket
		self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		self.host = socket.gethostbyname(self.host)
		self.port = 8080

		# file(s') header
		self.header_details = {}
		# list of files that are to be send
		self.filelist = []

		# Binding socket with the host and port
		self.sock_server.bind((self.host, self.port))
		self.sock_server.listen(5)

		print('Test server Listening on Host : {0}'.format(self.host))
		
		# Accepting the Connections of the client willing to connect
		self.connection, self.address = self.sock_server.accept()
		print(f"Connection from {self.address} (reciver) has been established!!!")


	def __loadFiles__(self):
		# Getting the filenames from the Input to send to the client
		# totalFiles = int(input("How many files you want to share: "))
		# filenames = []

		# for i in range(totalFiles):
		# 	filename = input("Enter the name (including complete path) of file-{}: ".format(i+1))
		# 	filenames.append(filename)


		files = input("Enter the names (including complete path) separated by comma (,): ").split(', ')

		return files


	def defining_header(self):
		self.filelist = self.__loadFiles__()

		temp_header = {}

		# Defining Data Dictionary Meta Data
		for i in range(len(self.filelist)):
			# Checking File Size
			filesize = os.stat(self.filelist[i]).st_size

			# Defining header to send as MetaData
			temp_header[i] = {
							'filename' : self.filelist[i],
							'filesize' : filesize,
						}

		return temp_header

	def send(self):
		
		self.header_details = self.defining_header()	# Calling function to defining the Header

		st = time.time()

		# Sending dictionary after converting into json object as byte data
		self.connection.send(bytes(json.dumps(self.header_details).encode()))
		print(self.header_details)

		# Looping over the list to send all the files in list
		for filename in self.filelist:

			# Opening and Reading the first chunk of file bytes
			with open(filename, 'rb') as f:
				file_data = f.read(CHUNK)

				# No Indentation Error Check
				while file_data:
					if not file_data:
						break
					# Sending Data through the connection to the client
					self.connection.send(file_data)
					# Reading the other chunks of the file bytes
					file_data = f.read(CHUNK)

			f.close()	# Closing the file

		et = time.time()
		print("\nFile(s) shared in {} seconds!".format((et-st)*1000))

		self.connection.close()	# Closing the connection
