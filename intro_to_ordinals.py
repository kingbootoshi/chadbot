import streamlit as st

st.set_page_config(
    page_title="The Ordinals Chadbot",
    page_icon='chadboo.png',
    layout='wide'
)

# CODE
st.header("Welcome to Immutability")

st.write("""
[![view source code ](https://ordinals.com/content/c17dd02a7f216f4b438ab1a303f518abfc4d4d01dcff8f023cf87c4403cb54cai0)](https://ordinals.com/inscription/2)""")

st.write("""
Welcome to your essential guide to Ordinals on the Bitcoin blockchain! Here, we turn every satoshi into something unique, offering endless possibilities for digital artifacts and inscriptions.

Explore this world with ease using our platform, featuring an expert chatbot ready to demystify Ordinals and Bitcoin for you. Whether you're a beginner or a pro, our Chadbot is here to help with any question.

Our website offers:

- Chatbot Guide: Engaging, easy-to-understand conversations with Chadbot.
- Ordinals Explained: A quick, clear intro to Ordinals.
- Interactive Learning: Master everything about Ordinals.
- Community Gateway: Connect with fellow Ordinals fans and creators.

Start your journey or get specific help through our menu. Your adventure in Bitcoin's unique digital world begins now!
""")

st.header("Access the Chatbot")

st.markdown(
    "<a href='https://chadbot.streamlit.app/ordinals_chatbot' target='_blank'>"
    "<button style='color: black; background-color: #f7931a; padding: 10px 24px; "
    "border-radius: 8px; border: none; cursor: pointer;'>"
    "Talk to Chadbot</button></a>", 
    unsafe_allow_html=True
)
