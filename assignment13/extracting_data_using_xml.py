# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL,
# read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_70010.xml (Sum ends with 48)

# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>

import urllib.parse as parse
import urllib.request as request
import xml.etree.ElementTree as ET

service_url = 'http://py4e-data.dr-chuck.met/'

address = input
try:
	fhand = request.urlopen('http://'+)
except Exception as e:
	raise e
