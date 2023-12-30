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

# Use this button to set the query parameters to navigate to the chatbot page
if st.button("Go to Chatbot"):
    # This will change the URL to include the query parameter for the chatbot page
    st.experimental_set_query_params(page="ordinals_chatbot")
    # Then you can check for this parameter in your main app script and render the appropriate page

st.header("Ordinals ELI5")

# Adding a button that toggles the explanation text
if st.button('Explain Ordinals like I\'m 5'):
    st.write("""
    Imagine Bitcoin is a huge, global piggy bank. Ordinals are like special stickers you can put on each coin (satoshi) in that piggy bank. Once a sticker is on a coin, it stays there forever and makes that coin unique. You can also draw on the coin, write a message, or even put a tiny picture on it. This way, you can collect, trade, and show off your special coins with their unique stickers to others!
    """)