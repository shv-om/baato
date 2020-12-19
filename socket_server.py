"""
Python code file for Server Side executables
"""

import os
import json
import socket

# Defining some Global Variables
CHUNK = 1024

class socket_server:

	def __init__(self):

		self.header_details = {}

		# Getting the filenames from the Input to send to the client
		self.filelist = input("Please provide the filename with extention to share separated by ',' : ").split(', ')

		# Creating Socket Object
		self.sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Defining Hostname and Port
		self.host = socket.gethostbyname('0.0.0.0')
		self.port = 8080

		# Binding socket with the host and port
		self.sock_server.bind((self.host, self.port))
		self.sock_server.listen(5)

		print('Test server Listening on Host : {0}'.format(self.host))

		# Accepting the Connections of the client willing to connect
		self.connection, self.address = self.sock_server.accept()
		print(f"Connection from {self.address} has been established!!!")


	def defining_header(self):
		i = 1
		temp_header = {}

		# Defining Data Dictionary Meta Data
		for filename in self.filelist:
			# Checking File Size
			filesize = os.stat(filename).st_size

			# Defining header to send as MetaData
			temp_header[i] = {
								'filename' : filename,
								'filesize' : filesize,
							}
			i += 1

		return temp_header

	def server(self):

		self.header_details = self.defining_header()	# Calling function to defining the Header

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

		print("Data has been transmitted successfully")

		self.connection.close()	# Closing the connection


server_object = socket_server()
server_object.server()
