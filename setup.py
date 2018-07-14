#!/usr/bin/env python3

import setuptools

import typing
import os
import sys

sys.path.insert(0, "src/")
import config as ITEST_Config

class CMakeExtension(setuptools.Extension):
    def __init__(self, name, sourcedir):
        super().__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(setuptools.command.build_ext):




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
        name=ITEST_Config.meta.name,
        version=ITEST_Config.meta.version,
        author=ITEST_Config.meta.author,
        author_email=ITEST_Config.meta.author_email,
        description=ITEST_Config.meta.description,
        license=ITEST_Config.meta.license,
        keywords=ITEST_Config.meta.keywords,
        url=,
        packages=,
        platforms=,
	long_description=_get_file_contents("README"),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: C",
        ]
)


