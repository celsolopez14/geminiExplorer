import os
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, ChatSession, Part, Content

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"replace with you json credential's path"

project_id = os.getenv("PROJECT_ID")
location = os.getenv("PROJECT_LOCATION")

vertexai.init(project=project_id, location=location)


#Helper function for handling and displaying messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query + ", speak like pirate, use emojis")
    response_message = response.candidates[0].content.parts[0].text 
    with st.chat_message("model"):
        st.markdown(response_message)

        st.session_state.messages.append({
            "role": "user",
            "content": query
        })

        st.session_state.messages.append({
            "role": "model",
            "content":response_message
        })


st.title("Gemini Explorer")

#Set default model
if "gemini_model" not in st.session_state:
    config = generative_models.GenerationConfig(
        temperature=0.4
    )
    model = GenerativeModel(
        "gemini-1.0-pro-001",
        generation_config=config
    )
    st.session_state["gemini_model"] = model
    st.session_state["chat_session"] = model.start_chat(response_validation=False)

#Init chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

#Get the user's name
user_name = st.text_input("Please enter your name:")


#Display messages from history
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role=message["role"],
        parts= [Part.from_text(message["content"])]
    )

    st.session_state.chat_session.history.append(content)

    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


#Initial prompt
if len(st.session_state.messages) == 0 and user_name:
    initial_prompt = f"Hello {user_name}, my name is ReX, I am an assistant powered by Google Gemini. How can I assist you today?"
    llm_function(st.session_state.chat_session, initial_prompt)

#Listen for user input
query = st.chat_input("Ask ReX anything...")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(st.session_state.chat_session, query)