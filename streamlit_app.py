# 
import streamlit as st
import requests
from lxml import html
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

nltk.download('punkt')
nltk.download('stopwords')

def fetch_blog_content(url):
    """Fetches and extracts content from the blog post."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            doc = html.fromstring(response.content)
            content = " ".join(doc.xpath('//text()'))
            return content
        else:
            return "Failed to fetch the content. Please check the URL."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def simple_answer_generation(content, query):
    """Generates a simple answer based on the content and query."""
    sentences = sent_tokenize(content)
    words = word_tokenize(query.lower())
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = [word for word in words if word not in stop_words]
    
    # Basic logic to find the best matching sentence
    best_match = ""
    max_match = 0
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        match_count = sum(1 for word in words if word in sentence_words)
        if match_count > max_match:
            max_match = match_count
            best_match = sentence
            
    return best_match if best_match else "Sorry, I couldn't find a relevant answer to your query."

def main():
    st.title("Blog Post Query Answering App")

    url = st.text_input("Enter the URL of the blog post:", "")
    user_query = st.text_input("Enter your query:", "")

    if st.button("Answer Query"):
        if url:
            content = fetch_blog_content(url)
            if content.startswith("Failed") or content.startswith("An error"):
                st.write(content)
            else:
                answer = simple_answer_generation(content, user_query)
                st.write(answer)
        else:
            st.write("Please enter a valid URL.")

if __name__ == "__main__":
    main()
