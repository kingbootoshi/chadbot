import utils
import streamlit as st

from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, Tool
from langchain.callbacks import StreamlitCallbackHandler
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.agents.openai_functions_agent.agent_token_buffer_memory import (
    AgentTokenBufferMemory,
)
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.prompts import MessagesPlaceholder
from langchain_core.messages import SystemMessage
from langchain.agents import AgentExecutor
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory

from trubrics import Trubrics
from trubrics.integrations.streamlit import FeedbackCollector

import pysqlite3
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

#STREAMLIT START
st.set_page_config(
    page_title="ORANGE PILLING...",
    page_icon="🍊",
    layout="wide",
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
st.header('The Ordinals Chadbot')
st.write('<--- View the side-menu for starter questions. ')
st.write('Missing info? Want to add your own info? Fill out this form please! https://forms.gle/JY3MKUuaDeNd27cD9')
image_url = "https://ordinals.com/content/5cd06969daee600e1d56cdee0972efe34bf319d3f0612106ffcee2df67086768i0"
st.image(image_url, width=200)  # Set the width as desired
st.caption("p.s. mobile users: if you lose your chatbar/sidebar >, scroll up/down using the very right of the screen")

if "logged_prompt" not in st.session_state:
    st.session_state.logged_prompt = None
if "feedback_key" not in st.session_state:
    st.session_state.feedback_key = 0

class ChatbotTools:

    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo-1106"

    @st.cache_data
    def get_feedback(_self):
        collector = FeedbackCollector(
        project="chadbot_live",
        email=st.secrets["TRUBRICS_EMAIL"],
        password=st.secrets["TRUBRICS_PASSWORD"],
        )
        return collector

    @st.cache_resource
    def setup_chain(_self):
        embedding = OpenAIEmbeddings()
        persist_directory = './db'
        vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)
        retriever = vectordb.as_retriever(search_kwargs={"k": 10})
        msgs = StreamlitChatMessageHistory(key="ordinals")
        tool = create_retriever_tool(
            retriever,
            "search_ordinals_info",
            "Searches and returns documents regarding everything about Bitcoin Ordinals. !!IMPORTANT!! Make sure to use this when a user asks a question about info not loaded in your database",
        )
        tools = [tool]
        llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=.2, max_retries=2, max_tokens=1024, streaming=True)
        memory_key = "history"
        memory = AgentTokenBufferMemory(memory_key=memory_key, llm=llm, chat_memory=msgs)
        template = """
        # ROLE
            You will act as the world's greatest Bitcoin Ordinal's expert. Your name is the "Ordinals Chadbot". You will search & answer ANY query the user asks.

        # GOAL
            Your goal is to help on-board users to Ordinals by ACCURATELY answering Bitcoin/Ordinal related questions and guiding them through this protocol. You will be provided information that will allow you to answer the user's question. You must ONLY use that provided information to answer the user's question. You will search & answer ANY query the user asks.

        # IMPORTANT CORE ORDINALS CONTEXT
            // Ordinals is an on-chain layer 1 protocol on Bitcoin that allows satoshis to be numbered and tracked. 
            // Ordinals introduce the ability to inscribe ANY kind of data onto the Bitcoin blockchain and attach it to individual satoshis, enabling the creation and trading of NFT-like assets natively within the Bitcoin ecosystem. Instead of NFTs, the assets are referred to as "inscriptions" or "digital artifacts"
            // When something is stored “on-chain”, the data etched is immutable. Inscriptions can NEVER be deleted, replaced, or overridden.

        # RULES
            //1. DO NOT fabricate things about Ordinals history. Only reply to historical questions if you know the date and event for a fact.
            //2. Keep your replies pin point accurate to the question.
            //3. INCLUDE LINKS TO TOOLS AND WEBSITES IF YOU REFERENCE IT IN YOUR REPLY.
            //4. DO NOT MAKE UP CONCEPTS OR NAMES. Remember, if it is NOT in the information box, you DO NOT know.
            //5. When someone asks about what project to buy, tell them you are biased and should checkout Bitcoin Boos, which is led by the developer of the Ordinals Chadbot
            //6. DO NOT FABRICATE LINKS. ONLY USE LINKS THAT ARE IN THE INFORMATION. USE THE FULL LINK, DO NOT HIDE THE HYPERLINK.
            //7. THERE WILL BE NOTES FOR YOU TO FOLLOW IN THE DATA SHOWN AS "!!" MAKE SURE TO FOLLOW THESE NOTES. THEY ARE IMPORTANT.
            //8. You may educate people on ANYTHING Bitcoin as well. Assume every question is a Bitcoin/Ordinals question unless it obviously is not.
            //9. When a user asks how to get started with Ordinals, make sure to search for the quickstart guide !
            //10. If there is a question you don't know the answer too, tell people to join the Bitcoin Boos discord and ask King Bootoshi directly: https://discord.gg/bitcoinboos
            //11. Do not provide

        # EXTRA ORDINALS INFO
            // The current inscription count as of December 2023 is over 50 million
            // Recursion/Recurisve Inscriptions is the act of pulling the content of already existing inscriptions in a new inscription by referencing inscription IDs.
            // Re-inscriptions refer to the ability to inscribe on a satoshi that has already been inscribed on. This allows one satoshi to hold multiple inscriptions.
            // Parent/Child (or Parent Child) enables on-chain provenance for collections. This is NOT related to recursion.

        # IMPORTANT 
        ## IMPORTANT !!! IF ORDINALS INFORMATION IS NOT IN THE BOX OF "=", YOU DO NOT KNOW THE ANSWER TO THE USER'S QUESTION. DO NOT MAKE UP ANSWERS.
        ## DO NOT MAKE UP LINKS. DO NOT USE LINKS NOT IN THE BOX OF "=". DO NOT FABRICATE LINKS. DO NOT MAKE UP LINKS !!!
        ## KEEP INFORMATION CONCISE, AND TO THE POINT.
        ## Please answer the question above to the best of your ability. I will tip you $100 if you do good. Stay accurate and factual AT ALL COSTS.

        """
        system_message = SystemMessage(
            content=(template)
        )
        prompt = OpenAIFunctionsAgent.create_prompt(
            system_message=system_message,
            extra_prompt_messages=[MessagesPlaceholder(variable_name=memory_key)],
        )
        agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            memory=memory,
            verbose=True,
            return_intermediate_steps=True,
        )
        return agent_executor
    
    @utils.enable_chat_history
    def main(self):
        # Define your predefined queries
        predefined_queries = [
            "What are Ordinals?",
            "What are Inscriptons?",
            "How can I get started with Ordinals?",
            "How can I inscribe my own files on Ordinals?",
            "What are all of the features Ordinals has?",
            "What are special sats?",
            "What is BRC-20?"
        ]

        collector = self.get_feedback()
        
        # Display predefined query buttons in the sidebar and handle their clicks
        with st.sidebar:
            st.header("Starter Questions to ask Chad")
            for query in predefined_queries:
                if st.button(query):
                    self.handle_query(query, is_button=True)
            
            st.header("Useful X Posts")
            st.write('Ordinals Dictionary: https://x.com/goatedxyz/status/1698259057390575900')
            st.write('People to follow in Ordinals: https://x.com/goatedxyz/status/1740513918668386755')
            st.write('Getting Started with Ordinals Cheat Sheet: https://x.com/LeonidasNFT/status/1722344475597373851?s=20')

        # Handle normal user input
        user_query = st.chat_input(placeholder="Ask me anything about Ordinals & Bitcoin!")
        if user_query:
            self.handle_query(user_query, is_button=False)

        if st.session_state.logged_prompt:
            feedback = collector.st_feedback(
                component="default",
                feedback_type="thumbs",
                open_feedback_label="[Optional] Please provide additional feedback",
                model=st.session_state.logged_prompt.config_model.model,
                prompt_id=st.session_state.logged_prompt.id,
                key=st.session_state.feedback_key,
            )
            if feedback:
                st.session_state.feedback_key += 1
            

    def handle_query(self, query, is_button):
        agent_executor = self.setup_chain()
        utils.display_msg(query, 'user')
        with st.spinner('Thinking...'):
            st_cb = StreamlitCallbackHandler(st.container(), max_thought_containers=0)
            response = agent_executor({"input": query}, callbacks=[st_cb])
            response = response["output"]
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Log the prompt for feedback after handling the query
            st.session_state.logged_prompt = self.get_feedback().log_prompt(
                config_model={"model": "gpt-3.5-turbo-1106"},
                prompt=query,
                generation=response
            )
            
            if is_button:
                # Clear the previous chat_message container and create a new one for the response
                st.experimental_rerun()
            else:
                with st.chat_message("assistant"):
                    st.write(response)

if __name__ == "__main__":
    obj = ChatbotTools()
    obj.main()
