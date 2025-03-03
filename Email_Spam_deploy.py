import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
import pickle
ps=PorterStemmer()

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email Spam Classifier")
input_email=st.text_input("Enter Message:")
if st.button('Predict'):
    transformed_email=transform_text(input_email)

    vector_input=tfidf.transform([transformed_email])

    res=model.predict(vector_input)[0]

    if res==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
