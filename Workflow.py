from Bio import Entrez
from Settings import EMAIL 
from Functions import PhenVar
from random import randint
from progressbar import ProgressBar

Entrez.email = EMAIL

IN = 'no'
while  IN == 'no':
	ID = PhenVar()
	print("\nIf you are satisfied with the results and want to continue with the analysis, please enter 'YES'.")
	IN = input("If you want to enter another rsID, please enter 'NO'. ").lower()
if IN != 'yes':
	print("\nYour answer was {}. You needed to enter either 'Yes' or 'No'. Please start again.".format(IN))
else:
	data =  Entrez.read(Entrez.elink(dbfrom='snp', db = 'pubmed', linkname='snp_pubmed_cited', id=ID))
	pmids =  [id_dict['Id'] for id_dict in data[0]['LinkSetDb'][0]["Link"]]
	rsids = []
	bar = ProgressBar()
	for pmid in bar(pmids):
		data = Entrez.read(Entrez.elink(dbfrom='pubmed',db='snp',linkname='pubmed_snp_cited',id=pmid))
		rsids.extend([id_dict['Id'] for id_dict in data[0]['LinkSetDb'][0]['Link']])
	rsids = [id for id in set(rsids)] #remove duplicates and turn dict to a list
	print('\n{} unique rsIDs were retrieved from {} PMIDs using rs{} as a search term'.format(len(rsids), len(pmids),ID))
	rnum = randint(1,1000)
	with open('temp_rsids{}.txt'.format(rnum), 'a+') as f:
		for item in rsids:
			f.write("rs{} ".format(item))


