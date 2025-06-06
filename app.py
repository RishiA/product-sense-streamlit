
import streamlit as st
from rag_engine import get_answer

st.set_page_config(page_title="Product Sense Budget Request Q&A", layout="wide")

# Custom CSS for improved aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fb;
        padding: 2rem;
    }
    .stTextInput > div > div > input {
        border-radius: 8px;
        padding: 0.75rem;
        border: 1px solid #ccc;
    }
    .response-box {
        background-color: #ffffff;
        padding: 1.5rem;
        margin-top: 1rem;
        border-left: 5px solid #4A90E2;
        border-radius: 6px;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.title("📌 Product Sense Course: Budget Request Q&A")

st.markdown("""
Welcome! This interactive assistant is part of my request to enroll in **Shreyas Doshi’s Product Sense** course.  
Use the input below to ask about the course, my rationale, or how it aligns with Justworks' goals.
""")

st.divider()

user_question = st.text_input("💬 Ask a question about the proposal or course:")
st.caption("💡 Try keywords like: **why this course**, **SUI**, **AI**, **share**")

if user_question:
    with st.spinner("Thinking..."):
        answer = get_answer(user_question)
        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.markdown("### 🤖 Answer")
        st.write(answer)
        st.markdown('</div>', unsafe_allow_html=True)
