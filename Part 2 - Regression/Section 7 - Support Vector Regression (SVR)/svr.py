import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")


X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2:3].values

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
sc_y = StandardScaler()
y = sc_y.fit_transform(y)

from sklearn.svm import SVR
regressor = SVR(kernel="rbf")
regressor.fit(X,y)

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))
print(y_pred)
plt.scatter(X,y, color="red")
plt.plot(X, regressor.predict(X), color="blue")
plt.title("Truth or Bluff (SVR)")
plt.xlabel("Position Label")
plt.ylabel("Salary")
plt.show()