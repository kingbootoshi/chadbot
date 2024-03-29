import streamlit as st

st.set_page_config(
    page_title="The Ordinals Chadbot",
    page_icon='chadboo.png',
    layout='wide',
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://discord.gg/ordinals",
        "Report a bug": "https://twitter.com/KingBootoshi",
        "About": """
            ## THE ORDINALS CHATBOT
            
            **Creator Twitter**: https://twitter.com/KingBootoshi\n
            **Data Repo**: https://github.com/kingbootoshi/ordinals_ai_data
            
            The AI Assistant named, The Ordinals Chatbot, is aimed to answer questions
            related to the Bitcoin Ordinals eco-system. Developed and created by King Bootoshi.
            DM him on Twitter if you have any questions or concerns.

        """
    }
)

# CODE
st.header("Welcome to Immutability")

st.write("""
[![view source code ](https://ordinals.com/content/c17dd02a7f216f4b438ab1a303f518abfc4d4d01dcff8f023cf87c4403cb54cai0)](https://ordinals.com/inscription/2)""")

st.write("""
Hi, we're your guide to Ordinals on the Bitcoin blockchain! 

Here, we turn every satoshi into something unique, offering endless possibilities for digital artifacts and inscriptions.

Explore this ecosystem with ease using our platform, featuring an expert chatbot ready to demystify Ordinals and Bitcoin for you. Whether you're a beginner or a pro, our Chadbot is here to help with any question.

Our website offers:

- Chatbot Guide: Engaging, easy-to-understand conversations with Chadbot.
- Ordinals Explained: A quick, clear intro to Ordinals.
- Interactive Learning: Master everything about Ordinals.

Your adventure in Bitcoin's unique digital world begins now!

Created by King Bootoshi of the Boo Kingdom. For more fun AI creations, visit https://twitter.com/BitcoinBoos
""")

st.header("Access the Chatbot")

st.markdown(
    "<a href='https://chadbot.streamlit.app/ordinals_chatbot' target='_blank'>"
    "<button style='color: black; background-color: #f7931a; padding: 10px 24px; "
    "border-radius: 8px; border: none; cursor: pointer;'>"
    "Talk to Chadbot</button></a>", 
    unsafe_allow_html=True
)
