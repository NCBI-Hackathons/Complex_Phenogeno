from Functions import clin_data, empirical_auc
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier 
import numpy as np
from progressbar import ProgressBar

clin_name = input("What is the name of the csv file holding the clinical data? \n (If using the toy datasets, the name should be: fertility)\n")
regressor = input("What is the name of the column in your clinical dataset {}.csv that holds the values of the risk factor (regressor)?".format(clin_name))
pct_train = float(input("What fraction of the clinical data do you want to use for training? (Recommended is 0.7) "))

print('##############	Calculating Linear Regression Model ########################')
bar1 = ProgressBar()
AUC_lm = []
for i in bar1(range(50)):
    data = clin_data(clin_name, pct_train, regressor)
    lm = linear_model.LinearRegression()
    lm.fit(data['train_X'], list(data['train_Y']))
    output_lm = lm.predict(data['test_X'])
    AUC_lm.append(empirical_auc(data,output_lm))
print("The AUC for the LM is {:.2f}, stdev = {:.2f}.".format(np.average(AUC_lm),np.std(AUC_lm)))

results = {key: [] for key in range(4,51,2)}
bar2 = ProgressBar()
print('##############	Calculating Random Forest Model ########################')
for j in bar2(range(50)):
    for i in range(4,51,2):
        forest = RandomForestClassifier(n_estimators = 200, min_samples_leaf = 0.05,  max_depth=i)
        forest.fit(data['train_X'], list(data['train_Y']))
        output_rf = forest.predict(data['test_X'])
        auc = empirical_auc(data,output_rf)
        results[i].append(auc) 
for i in range(4,51,2):
    print("Tree depth of {} has average AUC of {:.2f} with stdev {:.2f}".format(i, np.average(results[i]), np.std(results[i])))

mod = input("\n\nDo you want to proceed with the linear regression model (LR) or random forest (RF) model?").lower()
if mod == "lr":
    Y_hat = lm.predict(data['dataset'].drop(regressor, axis=1))
    e= np.subtract(data['dataset'][regressor], Y_hat)
    oe= data['dataset'][regressor]/ Y_hat
if mod == "rf":
    i = int(input("OK. What tree depth do you pick?"))
    forest = RandomForestClassifier(n_estimators = 200, min_samples_leaf = 0.05,  max_depth=i)
    forest.fit(data['train_X'], list(data['train_Y']))
    Y_hat = forest.predict(data['dataset'].drop(regressor, axis=1))
    e= np.subtract(data['dataset'][regressor], Y_hat)
    oe= data['dataset'][regressor]/ Y_hat
else:
    print("I am expecting either LR (linear regression) or RF (random forest). You entered {}.\n Nothing has been saved from this step". format(mod)).lower()

A = {'ID': list(data['dataset'].index), 'residual': [i for i in e] , 'o/e': [j for j in oe]} 
A = pd.DataFrame(A)
A.to_csv("./../Outputs/Clinical_deviations.csv", sep=",")
