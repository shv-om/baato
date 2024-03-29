"""
Python code file for Client Side executables
"""

import os
import json
import socket

# Defining some Global Variables
CHUNK = 1024

class socket_client:

	def __init__(self):

		# Creating Socket Object
		self.sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Input Hostname and define Port
		self.host = input("Host: ")
		self.port = 8080

		# Binding socket with the host and port
		try:
			self.sock_client.connect((self.host, self.port))
			print("Connected...")
		except ConnectionRefusedError:
			print("Currently server is down!! Try later!")


	def recieve(self):
		
		# Receiving the Header for the Main Data
		detail_header = self.sock_client.recv(CHUNK)

		# Loading the Json Data from the header received
		detail_header = json.loads(detail_header)
		print(detail_header)

		pathname = input("Enter a folder path where you want to recieve those files: ")

		for i in range(len(detail_header)):

			# Opening new file to write the receiving data
			filename = os.path.join(pathname, detail_header[str(i)]['filename'])

			with open(filename, 'wb') as f:
				print("file Opened")

				# Writing the received data to the file opened
				# Checking If the file size exceeds the original file size
				while detail_header[str(i)]['filesize'] > f.tell():
					file_data = self.sock_client.recv(CHUNK)
					
					if not file_data:	# Checking if the File Ends
						print("Here")
						break
					
					f.write(file_data)
				print(f.tell())

			f.close()

		print("File has been received...")

		self.sock_client.close()	# Closing the Connection