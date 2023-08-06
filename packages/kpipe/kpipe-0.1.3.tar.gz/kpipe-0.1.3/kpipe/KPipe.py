# MIT License

# Copyright (c) 2021 kaalam.ai The Authors of Jazz

# Hosted at https://github.com/kaalam/kpipe

import re


class KPipe():

	@staticmethod
	def zip_script_names():
		"^.*/scripts/([0-9]+)_([a-zA-Z][a-zA-Z0-9_]*)\\.py$"

	@staticmethod
	def info(calc_hashes = True):
		print('Called info(%s)' % (calc_hashes))
		return 0

	@staticmethod
	def make(force_rebuild = False):
		print('Called make(%s)' % (force_rebuild))
		return 0

	@staticmethod
	def help():
		usage = """
Usage:
------

  kpipe info  Lists all the scripts and data files including hashes and recency
              showing what needs rebuilding, if anything.
  kpipe fast  Same and info without computing the file hashes.
  kpipe make  Applies a "make algorithm" to build the files if either inputs or
              scripts have smaller recency than the output.
  kpipe build Rebuild everything in order, regardless of file recency.

(See: https://github.com/kaalam/kpipe/example for some example scripts.)
"""
		print(usage)
		return 1
