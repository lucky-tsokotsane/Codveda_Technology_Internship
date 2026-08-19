import pandas as pd, nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score

dataset = pd.read_csv('Data Set For Task/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data.csv').copy()
x_Text_trainData, x_Text_testData, y_Sentiment_trainData, y_Sentiment_testData = train_test_split(dataset["comment"], dataset["sentiment"], random_state=42, test_size=0.2, train_size=0.8)

stemmer = nltk.stem.PorterStemmer()
def Stemmer(comment):
    return [stemmer.stem(word) for word in comment.split()]

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

vectorizer = TfidfVectorizer(stop_words=stop_words, analyzer=Stemmer)
vectors_train = vectorizer.fit_transform(x_Text_trainData)
vectors_test = vectorizer.transform(x_Text_testData)

MLClassifier = MLPClassifier(max_iter=1500, learning_rate='adaptive')
MLClassifier.fit(vectors_train.toarray(), y_Sentiment_trainData)
MLVector_test = MLClassifier.predict(vectors_test.toarray())
print("Model Accuracy/Re-call_score:", MLClassifier.score(vectors_test.toarray(), y_Sentiment_testData), "f1-score:", f1_score(y_Sentiment_testData, MLVector_test, average='weighted'))