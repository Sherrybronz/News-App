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
            st.write(f"**URL:** {chosen_article['url']}")
API_KEY = '1d1d5237d98f465e84dd1c3fc9a75061'
topics = ['Technology', 'Sports', 'Health', 'Business','India','World','Gaming','Pune']

st.title("News App")
st.write("Select a topic to read news articles:")

topic = st.selectbox("Topic:", topics)

if topic:
    articles = fetch_news(API_KEY, topic)
    display_news(articles)
