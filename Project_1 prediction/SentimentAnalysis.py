import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

def train():
    columns = ['sentence', 'sentiment']
    df_1 = pd.read_csv('imdb_labelled.txt', sep='\t', header=None)
    df_2 = pd.read_csv('amazon_cells_labelled.txt', sep='\t', header=None)
    df_3 = pd.read_csv('yelp_labelled.txt', sep='\t', header=None)
    df = pd.concat((df_1, df_2, df_3))
    df.columns = columns
    X = df['sentence'].values
    y = df['sentiment'].values

    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(X)

    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)

    logistic = LogisticRegression()
    logistic.fit(x_train, y_train)
    return tfidf, logistic

def test(userInput):
    tfidf, log = train()
    review_tfidf = tfidf.transform([userInput])
    y_pred = log.predict(review_tfidf)
    # print(y_pred)
    if y_pred[0] == 0:
        pred = "Negative"
    else:
        pred = "Positive"
    # score = accuracy_score(y_test, y_pred)
    return pred