from Functions import clin_data, empirical_auc
from sklearn import linear_model
import numpy as np

clin_name = input("What is the name of the cvs file holding the clinical data? ")
pct_train = float(input("What fraction of the clinical data do you want to use for training? (Recommended is 0.7) "))

AUCs = []
for i in range(1000):
	data = clin_data(clin_name, pct_train)

	lm = linear_model.LinearRegression()
	lm.fit(data['train_X'], list(data['train_Y']))
	Y_hat_lm = lm.predict(data['test_X'])

	AUCs.append(empirical_auc(data,Y_hat_lm))
print(AUCs)



#e_lm = np.subtract(data['test_Y'], Y_hat_lm)
#oe_lm = data['test_Y']/ Y_hat_lm	