import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import f1_score

dataset = pd.read_csv(filepath_or_buffer='Data Set For Task/3) Sentiment dataset.csv').copy()
dataset.drop(labels=['Unnamed: 0.1', 'Unnamed: 0', 'Timestamp', 'User', 'Platform', 'Hashtags', 'Retweets', 'Likes', 'Country', 'Year', 'Month', 'Day', 'Hour'], axis=1, inplace=True)
x_Text_trainData, x_Text_testData, y_Sentiment_trainData, y_Sentiment_testData = train_test_split(dataset["Text"], dataset["Sentiment"], random_state=42, test_size=0.2, train_size=0.8)

vectorizer = TfidfVectorizer()
vectors_train = vectorizer.fit_transform(x_Text_trainData)
vectors_test = vectorizer.transform(x_Text_testData)

classifier = GaussianNB()
classifier.fit(vectors_train.toarray(), y_Sentiment_trainData)
y_pred = classifier.predict(vectors_test.toarray())
print(f1_score(y_Sentiment_testData, y_pred, average=None))