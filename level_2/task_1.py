import sklearn as sk, pandas as pd, matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

dataFrame = pd.read_csv("../Data Set For Task/Housing.csv")
x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(dataFrame["price"], dataFrame["area"], random_state=0, test_size=0.2)

Linearmodel = sk.linear_model.LinearRegression()
Linearmodel.fit(x_train.values.reshape(-1, 1), y_train)
y_linear = Linearmodel.predict(x_train.values.reshape(-1, 1))

RandomForestmodel = sk.ensemble.RandomForestRegressor(n_estimators=100, random_state=0)
RandomForestmodel.fit(x_train.values.reshape(-1, 1), y_train)
y_random_forest = RandomForestmodel.predict(x_train.values.reshape(-1, 1))

DecisionTreemodel = sk.tree.DecisionTreeRegressor(random_state=0)
DecisionTreemodel.fit(x_train.values.reshape(-1, 1), y_train)
y_decision_tree = DecisionTreemodel.predict(x_train.values.reshape(-1, 1))

print(f"LINEAR MODEL\nr2: {r2_score(y_train, y_linear):.2f} (r: {r2_score(y_train, y_linear)**(1/2):.2f})\nMSE: {mean_squared_error(y_train, y_linear):.2f} (RMSE: {mean_squared_error(y_train, y_linear)**(1/2):.2f})\nMAE: {mean_absolute_error(y_train, y_linear):.2f}\n")
print(f"RANDOM FOREST MODEL\nr2: {r2_score(y_train, y_random_forest):.2f} (r: {r2_score(y_train, y_random_forest)**(1/2):.2f})\nMSE: {mean_squared_error(y_train, y_random_forest):.2f} (RMSE: {mean_squared_error(y_train, y_random_forest)**(1/2):.2f})\nMAE: {mean_absolute_error(y_train, y_random_forest):.2f}\n")
print(f"DECISION TREE MODEL\nr2: {r2_score(y_train, y_decision_tree):.2f} (r: {r2_score(y_train, y_decision_tree)**(1/2):.2f})\nMSE: {mean_squared_error(y_train, y_decision_tree):.2f} (RMSE: {mean_squared_error(y_train, y_decision_tree)**(1/2):.2f})\nMAE: {mean_absolute_error(y_train, y_decision_tree):.2f}")