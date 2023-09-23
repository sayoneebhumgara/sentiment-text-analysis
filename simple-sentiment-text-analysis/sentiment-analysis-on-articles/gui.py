import tkinter as tk
from tkinter import ttk
from textblob import TextBlob
from newspaper import Article
import nltk

# Download the 'punkt' tokenizer data
nltk.download('punkt')

# Function to perform sentiment analysis
def analyze_sentiment():
    url = entry_url.get()
    article = Article(url)
    
    article.download()
    article.parse()
    article.nlp()

    text = article.text
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_type = "Positive"
        sentiment_color = "green"
    elif sentiment < 0:
        sentiment_type = "Negative"
        sentiment_color = "red"
    else:
        sentiment_type = "Neutral"
        sentiment_color = "black"

    # Display sentiment type in color
    sentiment_label.config(text=f"Sentiment: {sentiment_type}", foreground=sentiment_color)

    # Display sentiment score in color
    sentiment_score_label.config(text=f"Score: {sentiment:.2f}", foreground=sentiment_color)

# Create the main application window
root = tk.Tk()
root.title("Simple Sentiment Analysis Tool")

# Create a label for the URL input
url_label = ttk.Label(root, text="Enter URL:")
url_label.pack()

# Create an entry widget for the user to input the URL
entry_url = ttk.Entry(root, width=40)
entry_url.pack()

# Create a button to analyze sentiment
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

# Create a label to display the sentiment result
sentiment_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
sentiment_label.pack()

# Create a label to display the sentiment score
sentiment_score_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
sentiment_score_label.pack()

# Start the GUI application
root.mainloop()
