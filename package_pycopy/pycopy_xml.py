import sys
import xml.etree.ElementTree as ET

from os.path import join, isfile, isdir
from shutil import copyfile


def help(error=""):
	exit_code = 0
	if error != "":
		print("ERROR:")
		print(error)
		print()
		exit_code = 1

	print(f'Usage: {sys.argv[0]} [config]')
	print()
	print('Commands:')
	print('  -h --help    Displays this message')
	sys.exit(exit_code)


def get_files(file_path: str):
	"""Yields files in form of dicts
	"""

	if not file_path.endswith('.xml'):
		help("Bad config file extesion")

	if not isfile(file_path):
		help(f"The file {file_path} does not exist")

	root = ET.parse(file_path).getroot()

	if root.tag != 'config':
		help("Bad syntax of config file: root tag is invalid")

	for child in root:
		if child.tag == "file":
			yield child.attrib


def copy_file(src_path: str, dst_path: str, filename: str):
	"""Copies file from src_path to dst_path
	"""
	src = join(src_path, filename)

	if not isfile(src):
		help(f"The file {src} does not exist")

	if not isdir(dst_path):
		help(f"The directory {src} does not exist")
	
	dst = join(dst_path, filename)
	copyfile(src, dst)


def main():
	if len(sys.argv) < 2 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
		help()

	for arg in sys.argv[1:]:
		for obj in get_files(arg):
			src_path = obj.get('source_path')
			dst_path = obj.get('destination_path')
			filename = obj.get('file_name')

			copy_file(src_path, dst_path, filename)


if __name__ == '__main__':
	main()
