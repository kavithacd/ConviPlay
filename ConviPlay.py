import streamlit as st
import PyPDF2
from gtts import gTTS
uploaded_file = st.file_uploader("Please upload your document", type=["pdf"])
if uploaded_file is not None:
    pdfReader = PyPDF2.PdfFileReader(uploaded_file)
    n_pages = pdfReader.numPages
    this_doc = ''
    for i in range(n_pages):
        pageObj = pdfReader.getPage(i)
        this_text = pageObj.extractText()
        this_doc += this_text
    language = 'en'
    myobj = gTTS(text=this_doc, lang=language, slow=False)
    myobj.save("audio_book.mp3")
    st.write('Audio Book Uploaded. Play whenever you are ready to go!')

    audio_file = open('audio_book.mp3', 'rb')
    st.audio(audio_file, format='audio/mp3')