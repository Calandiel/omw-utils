import re

def remove_non_ascii(string):
	return re.sub('[^A-Za-z0-9.,?! ]+', '', string).strip()

def clear_bit(number, bit_position):
	mask = ~(1 << bit_position)
	return number & mask

def fix_file_name(file_name):
	if '\0' in file_name:
		file_name = file_name.replace('\0', '')
	if '\x00' in file_name:
		file_name = file_name.replace('\x00', '')
	if '\\' in file_name:
		file_name = file_name.replace('\\', '/')

	return file_name

def is_nth_bit_set(number, n):
	"""
	Check if the n-th bit of a 64-bit integer is set.

	:param number: The 64-bit integer to check.
	:param n: The 0-based bit position to check (0 <= n < 64).
	:return: True if the n-th bit is set, False otherwise.
	"""
	if n < 0 or n >= 64:
		raise ValueError("n must be in the range [0, 63]")

	# Create a mask with the n-th bit set
	mask = 1 << n
	# Use bitwise AND to check if the n-th bit is set
	return (number & mask) != 0

def sanitize_string(string):
	string = string.replace(':', '\:').replace('[', '\[').replace(']', '\]').replace('\0', '')
	return string
