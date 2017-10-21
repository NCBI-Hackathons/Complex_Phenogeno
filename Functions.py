def PhenVar():
	import webbrowser
	print("\nAs a first step, you will need to confirm that your querry rsID returns results from literature that are specific to your complex disease of interest.\n")
	ID =input("Please enter a querry rsID number (do not include the letters 'rs'): ")
	url = 'https://phenvar.colorado.edu/results/?rsids='+ID+'&visualization=png-wordcloud&visualization=js-graph&normalization_type=default'
	webbrowser.open_new(url)
	print("A new web browser window has opened that is showing the PhenVar results for rs{}".format(ID))
	return(ID)

def rev_dict(dictionary):
	''' 
	This function takes a dictionary with strings as keys and a single number as its value.
	It reverses it by grouping all the keys with the same numeric values together and using 
	that numeric value as the key of the new dictionary.
	'''
	newDict = {i:[] for i in set(dictionary.values())} 
	for i in dictionary.items():
		newDict[i[1]].append(str(i[0]))
	return(newDict)