import streamlit as st
import requests

def fetch_news(api_key, topic):
    url = f'https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        st.error(f"Error fetching news: {response.status_code}")
        return []

def display_news(articles):
    for i, article in enumerate(articles, start=1):
        st.write(f"{i}. {article['title']}")

    choices = st.multiselect("Select news articles to read:", [f"{i}. {article['title']}" for i, article in enumerate(articles, start=1)])
    if choices:
        for choice in choices:
            chosen_article = articles[int(choice.split(".")[0]) - 1]
            st.write(f"**Title:** {chosen_article['title']}")
            st.write(f"**Description:** {chosen_article['description']}")
            st.write(f"**Source:** {chosen_article['source']['name']}")
            st.write(f"**URL:** [Read more]({chosen_article['url']})")

API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
topics = ['Technology', 'Sports', 'Health', 'Business', 'India', 'World', 'Gaming']

st.markdown(
    """
    <style>
    body {
        background-image: url("https://wallpapers-clan.com/wallpapers/cute-anime-boy-art/");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("News App")
st.write("Select a topic to read news articles:")

topic = st.selectbox("Topic:", topics)

if topic:
    articles = fetch_news(API_KEY, topic)
    if articles:  # Check if articles are returned
        display_news(articles)
    else:
        st.write("No articles found for this topic.")
