import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌐 Language Translation Tool (Deep Translator)")

text = st.text_area("Enter text:")

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Marathi': 'mr',
    'French': 'fr',
    'German': 'de',
    'Spanish': 'es'
}

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(languages.keys()))
with col2:
    target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.error("Please enter some text!")
    else:
        translated = GoogleTranslator(source=languages[source],
                                      target=languages[target]).translate(text)
        st.subheader("Translated Text:")
        st.success(translated)
        st.code(translated)