import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='My Portfolio', page_icon=':tada:',layout='wide')

lottieurl='https://lottie.host/2a414a6c-e01c-413d-8f1b-34537354caaa/uWyZIT9P8E.json'
pro1_img=Image.open('images/port1.jpg')

def loadlottie(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def loadcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
loadcss('styles/style.css')

lottie=loadlottie(lottieurl)

# header section

with st.container():
    st.subheader('Hi, I am P S Veera Venkata Naga Saiteja :wave:')
    st.title("A Data Scientist From India")
    st.write('I am very passionate about ways to use python and it\'s related libraries to mine best insights and forecast from the data')

# about section

with st.container():
    st.write('---')
    lc,rc=st.columns((1,1.1))
    with lc:
        st.header('What I do')
        st.write('##')
        st.write(
            '''
            I am Currently in the final year of my Bachelor's Degree in Computer Science at Koneru lakshmaiah University.
            - I am Currently doing my reserach in the field of Artificial Intelligence, namely Gesture Intelligence a new intutive way of human computer interaction.
            - I am Currently doing professional certification from IBM in Data Science.
'''
        )


st.write("[Linkedin Profile >](https://www.linkedin.com/in/pandu-sri/)")

with rc:
    st_lottie(lottie,height=300,key='coding')

st.write('---')
with st.container():
    st.header('Projects')
    st.write('##')
    img,text=st.columns((2,3))
    
    with img:
        st.image(pro1_img,width=400)
    with text:
        st.subheader('Gesture Intelligence : A New Intutive way of Human Computer Interaction')
        st.write(
            '''
            - Gestures being the integral part of today's life,these gestures are incorporated into the world of technology using AI.
            - Gestures can be the better mode of communication between Humans and computers.
            - Here many number of labeled hand gestures are given to the model to learn them, to identify particular gesture and perform an action corresponding to gesture.
'''
        )
        st.markdown('[Project Git_repo](https://github.com/Saiteja-203/GestureDetection)')

with st.container():
    st.write('---')
    st.header('Get In Touch With Me!')
    st.write('##')
    contact='''
            <form action="https://formsubmit.co/sriveeravenkat3@email.com" method="POST">
            <input type='hidden' name='_captcha' value='false'>
            <input type="text" name="name" placeholder='Name' required>
            <input type="email" name="email" placeholder='Email' required>
            <textarea name='message' placeholder='Your message' required></textarea>
            <button type="submit">Send</button>
            </form>
            '''
    lc,rc=st.columns(2)
    with lc:
        st.markdown(contact,unsafe_allow_html=True)
    with rc:
        st.empty()




