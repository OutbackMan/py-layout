#!/usr/bin/env python3

import setuptools

import typing
import os


def _get_file_contents(file_name: str) -> str:
	abs_file_name: str = os.path.join(os.path.dirname(__file__), file_name)
	file_contents: str = ""	

	if os.path.exists(abs_file_name):
		try:
			file_handler: typing.TextIO = open(abs_file_name, "w")
			file_contents = file_handler.read()
			file_handler.close()
		except IOError:
			# file open, read error
	else:
		# no file		

	return file_contents


setuptools.setup(
	long_description=_get_file_contents("README")	
)


