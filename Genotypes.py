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

	import multiprocessing
	import progressbar
	from os import system
	from Functions import ExtractRsID

	bar = progressbar.ProgressBar()
	pool = multiprocessing.Pool(len(prefix)) # run as many processes as vcfs. The default is the number of CPU cores.
	results = [pool.apply_async( ExtractRsID, p ) for p in prefix]
	for result in bar(results):
		result.get()
	






