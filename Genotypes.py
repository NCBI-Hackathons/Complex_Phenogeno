from os import listdir
import re

files = listdir('./../Inputs')
vcf_files = re.findall('.vcf.gz', str(files))
if len(vcf_files) == 0:
	print("There are no vcf files in the Input/ directory.")
else:

	import multiprocessing
	import progressbar
	from os import system
	from Functions import ExtractRsID


