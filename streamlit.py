import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to fetch blog post content
def fetch_blog_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
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
