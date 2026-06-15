import streamlit as st

st.set_page_config(page_title="RAG Knowledge Assistant")

st.title("RAG Knowledge Assistant")
st.write("Ask a question about company policies.")

question = st.text_input("Your question")

if question:
    st.subheader("Retrieved Context")
    st.info("Employees receive 15 paid time off days per year.")

    st.subheader("Answer")
    st.success("Employees receive 15 paid time off days per year.")

    st.subheader("Source")
    st.write("pto_policy.txt")