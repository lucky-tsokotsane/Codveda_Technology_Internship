import seaborn as sns, matplotlib.pyplot as plt, pandas as pd

doc = pd.read_csv(r"./Data Set For Task/iris.csv", encoding='utf-8', index_col=0)
print(doc.head())