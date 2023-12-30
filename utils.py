import os
import random
import streamlit as st

#decorator
def enable_chat_history(func):
    if st.session_state.get('OPENAI_API_KEY'):

        # to clear chat history after swtching chatbot
        current_page = func.__qualname__
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = current_page
        if st.session_state["current_page"] != current_page:
            try:
                st.cache_resource.clear()
                del st.session_state["current_page"]
                del st.session_state["messages"]
            except:
                pass

        # to show chat history on ui
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        for msg in st.session_state["messages"]:
            st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def configure_openai_api_key():
    # Load the API key from the environment variable
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    
    # Check if the API key is available
    if openai_api_key:
        # Set the API key in Streamlit's session state and environment variable
        st.session_state['OPENAI_API_KEY'] = openai_api_key
        os.environ['OPENAI_API_KEY'] = openai_api_key
    else:
        # Display an error message if the API key is not found
        st.error("The OpenAI API key is missing from the .env file.")
        st.stop()
    
    return openai_api_key
