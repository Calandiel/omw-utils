import struct
import sys
import os
import zlib
from PIL import Image
import re
from openmwrecords import Record
from openmwutils import *

class Field:
	def __init__(self):
		self.name = 'xxxx'
		self.size = 0
		self.data = []

	def convert_to_dict(self, parent_record):
		if self.name == 'HEDR' and parent_record == 'TES3':
			version = str(round(10 * struct.unpack('f', self.data[0:4])[0])) # multiplying by 10 to avoid floating point inaccuracy in str formatting
			version = version[0] + '.' + version[1:]
			flags = struct.unpack('f', self.data[4:4+4])[0]
			name = sanitize_string(self.data[4+4:4+4+32].decode('ascii'))
			description = sanitize_string(self.data[4+4+32:4+4+32+256].decode('ascii'))
			record_count = struct.unpack('<L', self.data[4+4+32+256:4+4+32+256+4])[0]
			di = {}
			di['version'] = version
			di['company_name'] = name
			di['file_description'] = description
			di['record_count'] = record_count
			return di
		if self.name == 'MAST' and parent_record == 'TES3':
			string = sanitize_string(self.data.decode('ascii'))
			di = {}
			di['value'] = string
			return di
		if self.name == 'DATA' and parent_record == 'TES3':
			number = struct.unpack('<L', self.data)[0]
			di = {}
			di['value'] = number
			return di
		if self.name == 'FLTV' and parent_record == 'GLOB':
			number = struct.unpack('f', self.data)[0]
			di = {}
			di['value'] = number
			return di
		if self.name == 'FNAM' and parent_record == 'GLOB':
			di = {}
			di['value'] = self.data[0]
			return di
		if self.name == 'NAME' and (parent_record == 'GLOB' or parent_record == 'TES3'):
			string = sanitize_string(self.data.decode('ascii'))
			di = {}
			di['value'] = string
			return di
		else:
			raise Exception("UNKNOWN HEADER:", self.name, ' FOR PARENT: ', parent_record)


def read_record(file):
	record_name = file.read(4).decode('ascii')
	data_field_size = struct.unpack('<L', file.read(4))[0]
	if data_field_size <= 0:
		raise Exception("Data field size must be at least 1!")
	unused = struct.unpack('<L', file.read(4))[0]
	flags = struct.unpack('<L', file.read(4))[0]

	rec = Record()
	rec.name = record_name
	rec.size = data_field_size

	# TODO - parse flags here

	offset = 0
	while offset < data_field_size:
		offset += 4
		field_name = file.read(4).decode('ascii')

		offset += 4
		field_size = struct.unpack('<L', file.read(4))[0]

		offset += field_size
		field_data = file.read(field_size)

		field = Field()
		field.name = field_name
		field.size = field_size
		field.data = field_data

		rec.fields.append(field)

	return rec

def parse_binary_file(file_path):
	failed_files = []
	total_file_count = 0
	with open(file_path, 'rb') as file:

		tes3_record = read_record(file)

		if tes3_record.name != "TES3":
			raise ValueError("Invalid file format. Expected 'TES3', found " + str(tes3_record.name))

		record_count = tes3_record.fields[0].convert_to_dict(tes3_record.name)['record_count']
		final_value = tes3_record.convert_to_string()
		i = 0
		for f in range(record_count):
			i += 1
			if i % 50 == 0:
				print(i, '/', record_count)
			rec = read_record(file)
			# print(rec.name) # TO REMOVE
			final_value += rec.convert_to_string()
			final_value += '\n'

		with open('output.txt', 'w') as output_file:
			output_file.write(final_value)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python openmw-to-ini.py <file_path>")
		sys.exit(1)

	file_path = sys.argv[1]
	parse_binary_file(file_path)
