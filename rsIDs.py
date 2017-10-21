from Bio import Entrez
from Settings import EMAIL 
from Functions import PhenVar
from progressbar import ProgressBar

Entrez.email = EMAIL

##1. Enter custom rsID (requires some homework to find a 'good' rsID or simply rely on the feedback offered by PhenVar)
IN = 'no'

while  IN == 'no':
	ID = PhenVar()
	print("\nIf you are satisfied with the results and want to continue with the analysis, please enter 'YES'.")
	IN = input("If you want to enter another rsID, please enter 'NO'. ").lower()
if IN != 'yes':
	print("\nYour answer was {}. You needed to enter either 'Yes' or 'No'. Please start again.".format(IN))

##2. Retrive PMIDs and their associated rsIDs
else:
	data =  Entrez.read(Entrez.elink(dbfrom='snp', db = 'pubmed', linkname='snp_pubmed_cited', id=ID))
	pmids =  [id_dict['Id'] for id_dict in data[0]['LinkSetDb'][0]["Link"]]
	rsids = []	
	bar = ProgressBar()
	for pmid in bar(pmids):
		data = Entrez.read(Entrez.elink(dbfrom='pubmed',db='snp',linkname='pubmed_snp_cited',id=pmid))
		rsids.extend([id_dict['Id'] for id_dict in data[0]['LinkSetDb'][0]['Link']])
	#rsidSet = [id for id in set(rsids)] #remove duplicates and turn dict to a list
	print('\nA total of {} unique rsIDs were retrieved from {} PMIDs using rs{} as a search term'.format(len([id for id in set(rsids)]), len(pmids),ID))
	
##3. Filter rsIDs by supportive evidence (number of PMIDs referencing them together with the original rsID)
	from collections import Counter
	from Functions import rev_dict

	rsDict = rev_dict(Counter(rsids)) 
	numPmids = [i for i in set(rsDict.keys())]
	numPmids.sort()
	
	temp = rsDict.copy()
	for i in numPmids:
		temp.pop(i,0)
		print('{} rsIDs are cited by more than {} PMIDs'.format(len([item for sublist in temp.values() for item in sublist]), i))

	condition_filter = False
	while condition_filter == False:
		print("What is the minimum acceptable number of publications supporting each rsID you want to consider?")
		print("Possible values are between 1 and {}.".format(max(numPmids[0:len(numPmids)-1])))
		no = int(input(''))
		if no <= max(numPmids[0:len(numPmids)-1]):
			selected_rsids = []
			for i in numPmids[::-1]:
				if i >= no:
					selected_rsids.extend(rsDict[i])
			selected_rsids = set(selected_rsids)
			condition_filter = True
		else:
			print("You have not entered a value between 1 and {}. Please retry.\n".format(max(numPmids[0:len(numPmids)-1])))
	print('\nYou have selected to analyse {} different rsIDs that are co-cited together with rs{} (included).'.format(len(selected_rsids), ID))

	with open('./../Outputs/rsids.txt', 'a+') as f:
		for item in rsids:
			f.write("rs{} ".format(item))


