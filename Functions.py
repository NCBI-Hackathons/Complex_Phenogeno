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

def ExtractRsID(Prefix):
	'''The following function requires installation of plink 1.9 from https:
	//www.cog-genomics.org/plink2 at the PATH directory'''
	from os import system
	print("Processing {}".format(Prefix))
	system('plink --vcf ./../Inputs/{}.vcf.gz --recode --extract ./../Outputs/rsids.txt --out {}'.format(Prefix, Prefix))
	system('plink --file {} --recodeAD --out {}'.format(Prefix, Prefix))

def importRaw(Prefix):
	'''Imports and cleanups .raw files created by ExtractRsID'''
	import pandas as pd
	tab = pd.read_table(Prefix + '.raw', sep=' ')
	to_drop = [i for i in list(tab)[1:] if 'HET' in i or 'rs' not in i]
	tab.drop(to_drop, axis=1, inplace=True, errors='raise')
	return(tab)

def clin_data(name,pct_train):

    ''' This function reads in the csv file of the given name from Inputs, splits it randomly to
    train and test data according to the percentage of train data given,
    and returns the train and test, outputs(Y) and features(X) as a dictionary'''

    import pandas as pd
    import numpy as np

    data = pd.read_csv('./../Inputs/' + name + '.csv',sep = "," , index_col = 0)
    is_train = np.random.uniform(0, 1, len(data)) <= pct_train
    train_idx = [i[0] for i in zip(range(len(data)), is_train) if i[1]==True]
    test_idx = [i[0] for i in zip(range(len(data)), is_train) if i[1]==False]
    train_data = data.filter(items=train_idx, axis = 0)
    test_data = data.filter(items=test_idx, axis = 0)

    d = {
    'train_Y' : train_data[train_data.columns[0]],
    'test_Y' : test_data[test_data.columns[0]],
    'train_X' : train_data.drop(train_data.columns[0], axis=1),
    'test_X' : test_data.drop(test_data.columns[0],axis=1),
    'dataset' : data
    }
    return(d)

def empirical_auc(data, Y_hat):
    ''' data = is the dictionary returned from function clin_data()
        Y_hat = is the rpedicted values'''

    import pandas as pd

    TPR = []
    FPR = []
    ranges = range(min(data['test_Y'])+2 , max(data['test_Y'])-2 ,1)
    temp = pd.DataFrame({'obs': list(data['test_Y']), 'pred': Y_hat})

    for i in ranges:
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for j in range(len(temp)):
            if temp['obs'][j]>=i and temp['pred'][j]>=i:
                TP = TP + 1
            elif temp['obs'][j]<i and temp['pred'][j]<i:
                TN = TN + 1
            elif temp['obs'][j]>=i and temp['pred'][j]<i:
                FN = FN + 1
            elif temp['obs'][j]<i and temp['pred'][j]>=i:
                FP = FP + 1
            else:
                print("WTF")

        TPR.append(TP / (TP + FN))
        FPR.append(FP / (TN + FP))

    from numpy import trapz
    return(trapz(TPR[::-1], x=FPR[::-1]))
	 