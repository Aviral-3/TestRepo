import streamlit as st
import requests
from bs4 import BeautifulSoup

# Assuming fetch_blog_content and answer_query functions are defined as before

# Streamlit app main function
def main():
    st.title("Period Sleep Query Chatbot")

    # Display a text input widget for user queries
    user_query = st.text_input("Enter your question about sleep issues before your period:")

    if user_query:
        # Assuming the URL is fixed for this example
        url = "https://www.cranberry.fit/post/why-don-t-i-sleep-well-before-my-period"
        blog_content = fetch_blog_content(url)  # Fetch the blog post content
        if not blog_content.startswith("Failed") and not blog_content.startswith("Error"):
            answer = answer_query(user_query, blog_content)  # Get answer to the query
            st.write("Answer:", answer)
        else:
            st.error("Failed to fetch the blog content. Please try again later.")

if __name__ == "__main__":
    main()
