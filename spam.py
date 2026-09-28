import streamlit as st
import pickle

st.set_page_config(page_title='SPAM  DETECTOR', page_icon='✉️')

@st.cache_resource
def load_saved_files():
    model = pickle.load(open('spam_model.pkl', 'rb'))
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    return model, vectorizer

model, vectorizer = load_saved_files()

st.title('✉️  spam mail prediction app')

user_email = st.text_area('paste email message here : ', height=150)

if st.button('classsify email'):
    if user_email.strip() == "":
        st.warning('please enter some text')
    else:
        input_features = vectorizer.transform([user_email])
        prediction = model.predict(input_features)
        
        if prediction == 1:
            st.error('SPAM MAIL DETECTED')
        else:
            st.succes('HAM MAIL(legitimate)')