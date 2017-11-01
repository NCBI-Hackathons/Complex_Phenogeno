from os import listdir
import re


files = listdir('./../files')
vcfs = [i for i in filter(lambda x: x.endswith('.vcf.gz'), files)]
prefix = [re.sub('.vcf.gz', '', vcf) for vcf in vcfs]
if len(prefix) == 0:
	print("There are no vcf.gz files in the files/ directory.")
	print("Bye!")
	exit()
else:

	from multiprocessing import Pool
	from os import system
	from Functions import ExtractRsID
	import time

	print("Please stand by. Processing the VCF files might take a while, depending on their size.")
	start_time = time.time()
	pool = Pool()
	pool.map(ExtractRsID, prefix)
	print("---Processing {} VCFs took {} minutes ---".format(len(prefix), str((time.time() - start_time)/60)))

	from Functions import importRaw

	A = importRaw(prefix[0])
	for i in range(1,len(prefix)):
		B = importRaw(prefix[i])
		A = A.merge(B, how = 'outer', on = 'FID')
	print(A.head())
	A.to_csv("./../Outputs/Genotypes.csv", sep="\t")

	from os import system

	system('rm *.raw *.ped *.map *.nosex *.log')

	print("The rsID-specific genotypes of your cohort are now saved at Outputs/Genotypes.csv")




	






