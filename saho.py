import streamlit as st
import pandas as pd
from textblob import TextBlob

# Title of the app
st.title("Facebook Post Sentiment Analysis")

# Instructions
st.write("""
    Enter Facebook posts below to analyze their sentiment. 
    The sentiment analysis will give a polarity score ranging from -1 (negative) to 1 (positive).
""")

# Textbox for user input (multi-line)
user_input = st.text_area(
    "Enter Facebook post(s) here (one post per line):", 
    "I love spending time with my family!\nThis is the worst experience ever."
)

# Function to get sentiment polarity score
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a value between -1 and 1

# Process the input when the user provides some text
if user_input:
    # Split the user input into individual posts (separated by new lines)
    posts = user_input.split("\n")
    
    # Create a DataFrame with the posts
    df = pd.DataFrame(posts, columns=['Post'])
    
    # Apply sentiment analysis on each post
    df['Sentiment'] = df['Post'].apply(get_sentiment)
    
    # Display the resulting DataFrame
    st.write("Sentiment Analysis Results:")
    st.dataframe(df)
    
    # Optionally, display a bar chart of the sentiment scores
    st.bar_chart(df['Sentiment'])
