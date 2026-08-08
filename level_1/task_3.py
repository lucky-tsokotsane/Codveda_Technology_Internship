import seaborn as sns, pandas as pd, matplotlib.pyplot as plt

dataFrame = pd.read_csv(r"../Data Set For Task/1) iris.csv")

if __name__ == "__main__":
    print(f"""{list(dict(dataFrame["species"].value_counts()).keys())[0]}\t\t\t\t\t{list(dict(dataFrame["species"].value_counts()).keys())[1]}\t\t\t\t{list(dict(dataFrame["species"].value_counts()).keys())[2]}
Individual Average:\nsepal_length: {sum(list(dataFrame["sepal_length"])[:49+1])/50:.2f}\t\tsepal_length: {sum(list(dataFrame["sepal_length"])[49:49+50+1])/50:.2f}\t\tsepal_length: {sum(list(dataFrame["sepal_length"])[49+50+1:-1])/50:.2f}
sepal_width: {sum(list(dataFrame["sepal_width"])[:49+1])/50:.2f}\t\tsepal_width: {sum(list(dataFrame["sepal_width"])[49:49+50+1])/50:.2f}\t\tsepal_width: {sum(list(dataFrame["sepal_width"])[49+50+1:-1])/50:.2f}
petal_length: {sum(list(dataFrame["petal_length"])[:49+1])/50:.2f}\t\tpetal_length: {sum(list(dataFrame["petal_length"])[49:49+50+1])/50:.2f}\t\tpetal_length: {sum(list(dataFrame["petal_length"])[49+50+1:-1])/50:.2f}
petal_width: {sum(list(dataFrame["petal_width"])[:49+1])/50:.2f}\t\tpetal_width: {sum(list(dataFrame["petal_width"])[49:49+50+1])/50:.2f}\t\tpetal_width: {sum(list(dataFrame["petal_width"])[49+50+1:-1])/50:.2f}

Correlation:\n{dataFrame.corr(numeric_only=True)}

Mean:\n{dataFrame.mean(numeric_only=True)}

Median:\n{dataFrame.median(numeric_only=True)}

Variance:\n{dataFrame.var(numeric_only=True)}""")

    sns.pairplot(data=dataFrame, hue="species")
    plt.savefig("pairplot.png")

    sns.histplot(data=dataFrame)
    plt.savefig("histplot.png")

    sns.boxenplot(data=dataFrame)
    plt.savefig("boxplot.png")