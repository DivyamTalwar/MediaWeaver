import streamlit as st
from main import app
from langchain_core.messages import HumanMessage, AIMessage

st.title("MediaWeaver Agent")

user_prompt = st.text_input("Enter your prompt:")

if st.button("Run Agent"):
    if user_prompt:
        with st.spinner("Agent is running"):
            try:
                initial_state = {
                    "messages": [HumanMessage(content=user_prompt)]
                }
                result = app.invoke(initial_state)
                
                st.subheader("Final Answer")
                final_message = result['messages'][-1]
                st.markdown(final_message.content)
                st.success("Agent execution finished.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")
