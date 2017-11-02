from Functions import clin_data, empirical_auc
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier 
import numpy as np
from progressbar import ProgressBar

clin_name = input("What is the name of the csv file holding the clinical data? \n (If using the toy datasets, the name should be: fertility)\n")
regressor = input("What is the name of the column in your clinical dataset {} that holds the values of the risk factor (regressor)?".format(clin_name))
pct_train = float(input("What fraction of the clinical data do you want to use for training? (Recommended is 0.7) "))

print('##############	Calculating Linear Regression Model ########################')
bar1 = ProgressBar()
AUC_lm = []
for i in bar1(range(50)):
	data = clin_data(clin_name, pct_train, regressor)
    lm = linear_model.LinearRegression()
	lm.fit(data['train_X'], list(data['train_Y']))
	Y_hat_lm = lm.predict(data['test_X'])
    AUC_lm.append(empirical_auc(data,Y_hat_lm))
print("The AUC for the LM is {:.2f}, stdev = {:.2f}.".format(np.average(AUC_lm),np.std(AUC_lm)))

results = {key: [] for key in range(4,51,2)}
bar2 = ProgressBar()
print('##############	Calculating Random Forest Model ########################')
for j in bar2(range(50)):
    for i in range(4,51,2):
        forest = RandomForestClassifier(n_estimators = 200, min_samples_leaf = 0.05,  max_depth=i)
        forest.fit(data['train_X'], list(data['train_Y']))
        outputTest = forest.predict(data['test_X'])
        auc = empirical_auc(data,outputTest)
        results[i].append(auc) 
for i in range(4,51,2):
    print("Tree depth of {} has average AUC of {:.2f} with stdev {:.2f}".format(i, np.average(results[i]), np.std(results[i])))

answer = "no"
while answer == "no":
    mod = input("\n\nDo you want to proceed with the linear regression model (LR) or random forest (RF) model?").lower()
    if mod == "lr":
        e_lm = np.subtract(data['test_Y'], Y_hat_lm)
        oe_lm = data['test_Y']/ Y_hat_lm
    if mod == "rf":
    else:
        answer = input("I am expecting either LR (linear regression) or RF (random forest). You entered {}.\n Do you want to quit? (Yes/No)". format(mod)).lower()





depth = int(input("What tree depth do you want to use in the analysis? "))

forest = RandomForestClassifier(n_estimators = 200, max_depth=depth)
forest.fit(data['train_X'], list(data['train_Y']))
Y_hat_rf = forest.predict(data['test_X'])






#e_rf = np.subtract(data['test_Y'], Y_hat_lm)
#oe_rf = data['test_Y']/ Y_hat_lm	

#data

#print("")
