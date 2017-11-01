from Functions import clin_data, empirical_auc
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier 
import numpy as np
from progressbar import ProgressBar


clin_name = input("What is the name of the cvs file holding the clinical data? ")
pct_train = float(input("What fraction of the clinical data do you want to use for training? (Recommended is 0.7) "))

# Linear model (reference)

bar1 = ProgressBar()
AUC_lm = []
for i in bar1(range(1000)):
	data = clin_data(clin_name, pct_train)

	lm = linear_model.LinearRegression()
	lm.fit(data['train_X'], list(data['train_Y']))
	Y_hat_lm = lm.predict(data['test_X'])

	AUC_lm.append(empirical_auc(data,Y_hat_lm))
print("The AUC for the LM is {:.2f}, stdev = {:.2f}.".format(np.average(AUC_lm),np.std(AUC_lm)))

#e_lm = np.subtract(data['test_Y'], Y_hat_lm)
#oe_lm = data['test_Y']/ Y_hat_lm	

#Random forest

results = {key: [] for key in range(4,51,2)}

bar2 = ProgressBar()

#Identify optimal parameters
for j in bar2(range(50)):
    for i in range(4,51,2):
        forest = RandomForestClassifier(n_estimators = 200, max_depth=i)
        forest.fit(data['train_X'], list(data['train_Y']))
        #Test the prediction
        outputTest = forest.predict(data['test_X'])
        auc = empirical_auc(data,outputTest)
        results[i].append(auc) 

for i in range(4,51,2):
    print("Tree depth of {} has average AUC of {} with stdev {}".format(i, np.average(results[i]), np.std(results[i])))

depth = int(input("What tree depth do you want to use in the analysis? "))

forest = RandomForestClassifier(n_estimators = 200, max_depth=depth)
forest.fit(data['train_X'], list(data['train_Y']))
Y_hat_rf = forest.predict(data['test_X'])

#e_rf = np.subtract(data['test_Y'], Y_hat_lm)
#oe_rf = data['test_Y']/ Y_hat_lm	

#data

#print("")
