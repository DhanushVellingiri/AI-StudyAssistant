import streamlit as st
from main import process_pdf, query_notes
import os

st.title("🧠 AI Study Assistant (Offline)")

if "chunks" not in st.session_state:
    st.session_state.chunks = None
    st.session_state.index = None

uploaded_file = st.file_uploader("Upload your lecture PDF")

if uploaded_file:
    os.makedirs("temp", exist_ok=True)  # ✅ Create temp folder if missing

    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    chunks, index = process_pdf(file_path)
    st.session_state.chunks = chunks
    st.session_state.index = index
    st.success("PDF processed!")

if st.session_state.chunks:
    question = st.text_input("Ask something about your notes")
    if st.button("Ask"):
        with st.spinner("Thinking..."):
            answer = query_notes(question, st.session_state.chunks, st.session_state.index)
            st.markdown(f"**Answer:** {answer}")
