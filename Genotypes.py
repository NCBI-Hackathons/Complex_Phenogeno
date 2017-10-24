from os import listdir
import re

files = listdir('./../Inputs')
vcfs = [i for i in filter(lambda x: x.endswith('.vcf.gz'), files)]
prefix = [re.sub('.vcf.gz', '', vcf) for vcf in vcfs]
if len(prefix) == 0:
	print("There are no vcf.gz files in the Inputs/ directory.")
	print("Bye!")
	exit()
else:

	from multiprocessing import Pool
	from os import system
	from Functions import ExtractRsID
	import time

	start_time = time.time()
	pool = Pool()
	pool.map(ExtractRsID, prefix)
	print("--- {} minutes ---".format(str((time.time() - start_time)/60)))


	






