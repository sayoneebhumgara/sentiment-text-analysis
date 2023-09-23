import tkinter as tk
from tkinter import ttk
from textblob import TextBlob
import nltk

# Download the 'punkt' tokenizer data
nltk.download('punkt')

# Function to perform sentiment analysis
def analyze_sentiment():
    text = text_entry.get("1.0", tk.END)  # Get the user-provided text from the Text widget
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        sentiment_type = "Positive"
        color = "green"
    elif sentiment < 0:
        sentiment_type = "Negative"
        color = "red"
    else:
        sentiment_type = "Neutral"
        color = "blue"

    result_label.config(text=f"Sentiment: {sentiment_type}, Score: {sentiment:.2f}", foreground=color)

# Create the main application window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Create a label for the user to enter text
text_label = ttk.Label(root, text="Enter Text:")
text_label.pack(pady=10)

# Create a Text widget for the user to input text
text_entry = tk.Text(root, width=40, height=10, wrap=tk.WORD)
text_entry.pack()

# Create a button to analyze sentiment
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=10)

# Create a label to display the sentiment result
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

# Center the window on the screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# Start the GUI application
root.mainloop()
