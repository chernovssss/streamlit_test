import streamlit as st

st.set_page_config(layout="wide", page_title="My Streamlit App", page_icon="🎉")

st.title("Hello, World!")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1.")
    st.checkbox("Checkbox 1")
with col2:
    st.header("Column 2")
    st.write("This is column 2.")
    st.selectbox("Selectbox 1", ["Option 1", "Option 2", "Option 3"])
with col3:
    st.header("Column 3")
    st.write("This is column 3.")
