import openai
import streamlit as st
import time
from classes.assistant import Assistant

assistant_id = st.secrets["ASSISTANT_ID"]

client = Assistant(openai_api_key=st.secrets["OPEN_AI_API_KEY"]).get_client()

if "start_chat" not in st.session_state:
    st.session_state.start_chat = False
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

st.set_page_config(page_title="Numainda", page_icon=":speech_balloon:")

st.title("Numainda",)
st.image('Numainda no BG Logo.png')
st.write("A knowledge bot designed to engage and educate on Pakistan's rich legal and parliamentary heritage. Drawing on the Constitution of Pakistan, the Elections Act 2017, and the latest parliamentary proceedings, Numainda shares fascinating legal and legislative facts in a fun, engaging manner.")

st.markdown("""*Things You Can Ask Me:*
            
                * Tell me an interesting fact from the constitution of Pakistan.
            
    * What is the role of the Parliament in Pakistan?
            
    * What happened in the parliament on 15th march 2024?
            """)


if st.button("Start Chat"):
    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

# if st.button("Exit Chat"):
#     st.session_state.messages = []  # Clear the chat history
#     st.session_state.start_chat = False  # Reset the chat state
#     st.session_state.thread_id = None

if st.session_state.start_chat:
    if "openai_model" not in st.session_state:
        st.session_state.openai_model = "gpt-4-1106-preview"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can i help?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        client.beta.threads.messages.create(
                thread_id=st.session_state.thread_id,
                role="user",
                content=prompt
            )
        
        run = client.beta.threads.runs.create(
            thread_id=st.session_state.thread_id,
            assistant_id=assistant_id,
            instructions="Please answer the queries of the user that they put in the prompt using the documents in your knowledge and nothing else.",
        )

        while run.status != 'completed':
            time.sleep(1)
            run = client.beta.threads.runs.retrieve(
                thread_id=st.session_state.thread_id,
                run_id=run.id
            )
        messages = client.beta.threads.messages.list(
            thread_id=st.session_state.thread_id
        )

        # Process and display assistant messages
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            st.session_state.messages.append({"role": "assistant", "content": message.content[0].text.value})
            with st.chat_message("assistant"):
                st.markdown(message.content[0].text.value)

else:
    st.write("Click 'Start Chat' to begin.")