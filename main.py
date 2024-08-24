import streamlit as st
import random
import time


st.set_page_config(
    page_title="Home",
    page_icon="logo.png"
)

if "messages" not in st.session_state:
    st.session_state.messages = []


# response 

def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)



st.sidebar.title("Welcome to Law Buddy")
uploaded_file = st.sidebar.file_uploader("Upload your case", type=["pdf", "docx", "txt"])
st.title("Chat with Law Buddy")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your query here..."):
    st.chat_message("user",avatar="😃").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})


    response = f"Buddy: {prompt} "
    

    with st.chat_message("assistant",avatar="bot.png"):
        response = st.write_stream(response_generator())
# Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


