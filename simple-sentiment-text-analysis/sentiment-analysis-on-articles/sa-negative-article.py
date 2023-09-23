from textblob import TextBlob
from newspaper import Article
import nltk

# Download the 'punkt' tokenizer data
nltk.download('punkt')


#negative article

url = 'https://economictimes.indiatimes.com/news/new-updates/sleep-deprivation-linked-to-brain-damage-and-alzheimers-risk-reveals-news-study/articleshow/103547875.cms'
article = Article(url)

article.download()
article.parse()
article.nlp()


text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)