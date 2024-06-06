import struct
from enum import Enum
from openmw_utils import *
from openmw_defs import *
from openmw_format import *

class Record:
	def __init__(self):
		self.name = 'xxxx'
		self.size = 0

		self.deleted = False
		self.persistent_reference = False
		self.initially_disabled = False
		self.blocked = False

		self.fields = []

	def convert_to_string(self):
		record_definition = next((x for x in ALL_RECORDS if x.name == self.name), None)
		if record_definition == None:
			raise Exception(f"No record definition for {self.name}")

		r = f"""[RECORD:{record_definition.name}]
"""
		for field in self.fields:
			# print('>',field.name) # TO REMOVE
			r += record_definition.convert_field(field)

		# print(r) # TO REMOVE
		return r
