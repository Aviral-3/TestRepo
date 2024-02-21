# # 
# import streamlit as st
# import requests
# from lxml import html
# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from string import punctuation

# nltk.download('punkt')
# nltk.download('stopwords')

# def fetch_blog_content(url):
#     """Fetches and extracts content from the blog post."""
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             doc = html.fromstring(response.content)
#             content = " ".join(doc.xpath('//text()'))
#             return content
#         else:
#             return "Failed to fetch the content. Please check the URL."
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# def simple_answer_generation(content, query):
#     """Generates a simple answer based on the content and query."""
#     sentences = sent_tokenize(content)
#     words = word_tokenize(query.lower())
#     stop_words = set(stopwords.words('english') + list(punctuation))
#     words = [word for word in words if word not in stop_words]
    
#     # Basic logic to find the best matching sentence
#     best_match = ""
#     max_match = 0
#     for sentence in sentences:
#         sentence_words = word_tokenize(sentence.lower())
#         match_count = sum(1 for word in words if word in sentence_words)
#         if match_count > max_match:
#             max_match = match_count
#             best_match = sentence
            
#     return best_match if best_match else "Sorry, I couldn't find a relevant answer to your query."

# def main():
#     st.title("Blog Post Query Answering App")

#     url = st.text_input("Enter the URL of the blog post:", "")
#     user_query = st.text_input("Enter your query:", "")

#     if st.button("Answer Query"):
#         if url:
#             content = fetch_blog_content(url)
#             if content.startswith("Failed") or content.startswith("An error"):
#                 st.write(content)
#             else:
#                 answer = simple_answer_generation(content, user_query)
#                 st.write(answer)
#         else:
#             st.write("Please enter a valid URL.")

# if __name__ == "__main__":
#     main()


import streamlit as st
import requests
from bs4 import BeautifulSoup as B

# Function to fetch blog post content
def fetch_blog_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = B(response.content, 'html.parser')
            # Adjust the selector based on the actual HTML structure of the blog
            main_content = soup.find('div', class_='post-content')  # Placeholder class
            text_content = " ".join(main_content.stripped_strings) if main_content else "Content not found."
            return text_content
        else:
            return "Failed to fetch content: HTTP Status Code {}".format(response.status_code)
    except Exception as e:
        return "Error fetching content: " + str(e)

# Dummy function for answering queries based on content
# In a real-world scenario, you'd implement more sophisticated logic here
def answer_query(query, content):
    if "sleep" in query.lower():
        return "This is a placeholder response related to sleep issues. For specific information, please refer to the blog content directly."
    return "Query not recognized. Please ask something else."

# Streamlit app starts here
st.title('Sleep Well Before Period FAQ Bot')

# You can make the URL dynamic or fixed depending on your need
url = 'https://www.cranberry.fit/post/why-don-t-i-sleep-well-before-my-period'
content = fetch_blog_content(url)

if content.startswith("Failed") or content.startswith("Error"):
    st.error(content)
else:
    query = st.text_input('Enter your question about sleep issues before periods:')
    if query:
        answer = answer_query(query, content)
        st.write('Answer:', answer)