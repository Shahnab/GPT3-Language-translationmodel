import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3898/3898150.png", width=100)
st.sidebar.subheader("About the GPT3 Language Translation Model :")
st.sidebar.markdown("##### This tool allows users to type queries in local language and generates output in local language")
st.sidebar.markdown("##### The model uses OpenAI text-davinci-003 Chat Model and facebook/m2m100_1.2B Translation Model")

st.sidebar.subheader("How to use:")
st.sidebar.markdown("##### Kindly choose the prefered language, provide OpenAI api-key and ask queries to the GPT-3 model ")

st.sidebar.subheader("About the GPT-3 Model:")
st.sidebar.markdown("##### Davinci is the most capable model in GPT-3 and can do anything that any other model can do, and much more—often with fewer instructions")
st.sidebar.markdown("Davinci is able to solve logic problems, determine cause and effect, understand the intent of text, produce creative content, explain character motives, and handle complex summarization tasks")

st.sidebar.subheader("Powered by")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/1280px-OpenAI_Logo.svg.png", width=150)

st.sidebar.caption("Streamlit App by </Shahnab>")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://shad0ws-gpt3translationmodel.hf.space", width=1100, height=650, scrolling=True)
