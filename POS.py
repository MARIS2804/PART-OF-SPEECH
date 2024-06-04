import streamlit as st
import spacy
from spacy import displacy
a=st.text_input("GIVE ANY TEXT")
nlp=spacy.load("en_core_web_sm")
doc=nlp(a)
html=displacy.render(doc,style="dep")
st.markdown(html,unsafe_allow_html=True)
   