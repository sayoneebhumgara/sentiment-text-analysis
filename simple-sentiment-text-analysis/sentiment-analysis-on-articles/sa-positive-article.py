from textblob import TextBlob
from newspaper import Article
import nltk

# Download the 'punkt' tokenizer data
nltk.download('punkt')
#positive article
url = 'https://www.fibre2fashion.com/industry-article/6339/the-power-of-positive'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)