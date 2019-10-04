#!/usr/bin/python
# -*- coding: utf-8 -*-

# Usage: run.py inputfilename.ext outputfilename.ext
# Example: run.py Mon-non-unicode.txt unicode.txt
import codecs
import libMon2uni
import sys

if len(sys.argv) < 3:
  sys.exit("Missing Parameters. \nUSAGE: Mon2uni mydatabase.sql mynewdatabase.sql")
if len(sys.argv) >3:
  sys.exit("Only two options required. More than two given. Check usage. \nUSAGE: Mon2uni input_file output_file")
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
input_file = codecs.open(input_file_name,encoding='UTF-8')
output_file = codecs.open(output_file_name,encoding='UTF-8', mode='w')

for input_line in input_file:
  input_line = libMon2uni.convert(input_line)
  output_file.write(input_line)
  output_file.flush()

input_file.close()
output_file.close()
