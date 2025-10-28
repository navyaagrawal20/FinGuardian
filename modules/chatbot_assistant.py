from utils.tutor_bot import tutor_response

def finbot_sidebar(profile=None):
import streamlit as st
with st.expander("🤖 FinBot – Your BFSI AI Assistant", expanded=False):
st.markdown("Ask anything about mutual funds, EMIs, credit score, or policies.")
query = st.text_input("Type your question here", key="chatbot_query")
level = st.selectbox("Your Financial Knowledge", ["Beginner", "Intermediate", "Expert"], key="chatbot_level")


if st.button("💬 Ask FinBot", key="chatbot_button"):
    if query:
        with st.spinner("Thinking..."):
            answer = tutor_response(query, level, profile=profile)
        st.success("✅ Here's what FinBot says:")
        st.markdown(answer)
    else:
        st.info("Type a question to ask FinBot.")