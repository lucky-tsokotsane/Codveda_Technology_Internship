import sklearn as sk, pandas as pd, matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

dataFrame = pd.read_csv("Data Set For Task/Housing.csv")
x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(dataFrame["price"], dataFrame["area"], random_state=0, test_size=0.2)

Linearmodel = sk.linear_model.LinearRegression()
Linearmodel.fit(x_train.values.reshape(-1, 1), y_train)
y_linear = Linearmodel.predict(x_train.values.reshape(-1, 1))
linear_string = f'''LINEAR MODEL
model accuracy: {r2_score(y_train, y_linear):.3f}
mse: {mean_squared_error(y_train, y_linear):.3f}
mae: {mean_absolute_error(y_train, y_linear):.3f}'''
plt.plot(x_train, y_linear, color='red', label='Training Data')

NeuralNetworkmodel = sk.neural_network.MLPRegressor()
NeuralNetworkmodel.fit(x_train.values.reshape(-1, 1), y_train)
y_NeuralNetwork = NeuralNetworkmodel.predict(x_train.values.reshape(-1, 1))
neural_string = f'''NEURAL NETWORK
model accuracy: {r2_score(y_train, y_NeuralNetwork):.3f}
mse: {mean_squared_error(y_train, y_NeuralNetwork):.3f}
mae: {mean_absolute_error(y_train, y_NeuralNetwork):.3f}'''
plt.plot(x_train, y_NeuralNetwork, color='blue', label='Training Data')

plt.scatter(x_test, y_test, color='green', label='Testing Data')
plt.scatter(x_train, y_train, color='black', label='Linear Model')
plt.xlabel('Price')
plt.ylabel('Area')
plt.savefig('images/NeuralNetwork.png')

print(linear_string+'\n\n'+neural_string)