import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='My Portfolio', page_icon=':tada:',layout='wide')

lottieurl='https://lottie.host/2a414a6c-e01c-413d-8f1b-34537354caaa/uWyZIT9P8E.json'
pro1_img=Image.open('images/port1.jpg')
pro2_img=Image.open('images/Pro2.jpg')

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
    st.title("AI Enthusiast | Problem Solver | Collaborator")
    st.subheader("Driven by Curiosity, Fueled by Innovation")

# about section

with st.container():
    st.write('---')
    lc,rc=st.columns((1,1.1))
    with lc:
        st.header('What I’m Passionate About')
        st.write(
            '''
I’m passionate about using technology to create innovative solutions that make a real difference. Whether it's building AI-driven applications, improving user experiences using web tools, or enhancing collaboration through technology. My interests lie in problem-solving, continuous learning, and exploring how tech can positively impact society. I am also deeply committed to fostering teamwork and leadership, which I’ve cultivated through my experience in leading and organizing events during my undergraduate years as Vice President of the Digital Twin Technology Club.'''
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
        st.subheader('Gesture Intelligence : An intuitive way of human-computer interaction.')
        st.write(
            '''
            - Gestures being the integral part of today's life,these gestures are incorporated into the world of technology using AI.
            - Gestures can be the better mode of communication between Humans and computers.
            - Here many number of labeled hand gestures are given to the model to learn them, to identify particular gesture and perform an action corresponding to gesture.
'''
        )
        st.markdown('[Project Git_repo](https://github.com/Saiteja-203/GestureDetection)')

    with img:
        st.image(pro2_img,width=400)
    with text:
        st.subheader('Dictionary Web Application')
        st.write(
            '''
            -  Designed and developed a web-based dictionary application using
               Python’s Streamlit library, to deliver a seamless user experience.
            - Implemented a search functionality, leveraging API integration to
              retrieve accurate word meanings.
'''
        )
        st.markdown('[Project Git_repo](https://github.com/Saiteja-203/Dictionary)')

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




