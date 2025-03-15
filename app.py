import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='My Portfolio', page_icon=':tada:',layout='wide')

lottie1url='https://lottie.host/2a414a6c-e01c-413d-8f1b-34537354caaa/uWyZIT9P8E.json'
lottie2url='https://lottie.host/71e523af-167c-4925-b1da-1ee25b50f429/FZFJZbeaFO.json'
pro1_img=Image.open('images/port1.jpg')
pro2_img=Image.open('images/Pro2.png')
pro3_img=Image.open('images/image.png')
cer1_img=Image.open('images/imageCer1.png')
cer2_img=Image.open('images/imageCer2.png')

def loadlottie(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def loadcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
loadcss('styles/style.css')

lottie1=loadlottie(lottie1url)
lottie2=loadlottie(lottie2url)

# header section

with st.container():
    lc,rc=st.columns((1.5,1))
    with lc:
        st.subheader('Hi, I am Prathipati P S Veera Venkata Naga Saiteja :wave:')
        st.title("Entrepreneur-in-the-Making | AI & Business Enthusiast")
        st.subheader("Driven by Curiosity, Fueled by Innovation")
    with rc:
        st_lottie(lottie2,height=300,key='hello')

# about section

with st.container():
    st.write('---')
    lc,rc=st.columns((1,1.1))
    with lc:
        st.header('About Me')
        st.write(
            '''With a keen interest in AI and business, and currently attending the 7-week Y Combinator Startup School program, I aspire to combine my technical expertise with entrepreneurial vision. I am always open to learning, collaborating, and exploring new opportunities that align with my goal of building and growing a successful startup.'''
        )

st.write("[Linkedin Profile >](https://www.linkedin.com/in/pandu-sri/)")

with rc:
    st_lottie(lottie1,height=300,key='coding')

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
    
    with img:
        st.image(pro3_img,width=400)
    with text:
        st.subheader('AI Chatbot')
        st.write(
            '''
            - Built a chatbot using Hugging Face pre-trained models, integrated it with a Flask web application for real-time conversations, designed a simple user interface to improve interaction quality.
'''
        )

st.write('---')
with st.container():
    st.header('Certifications')
    st.write('##')
    img,text=st.columns((2,3))
    
    with img:
        st.image(cer1_img,width=400)
    with text:
        st.subheader('City of Moreton Bay Entrepreneurship and Innovation Job Simulation on Forage - February 2025')
        st.write(
            '''
            - Completed a job simulation that gave insight into the tasks and challenges that entrepreneurs face.
            - Created a pitch deck to send to Venture Capital firms for pre-seed investment.
            - Used Wordpress to create a one page website, with the goal of convincing viewers that the product or service is worth buying.
'''
        )
    
    with img:
        st.image(cer2_img,width=400)
    with text:
        st.subheader('PwC Switzerland Cybersecurity Job Simulation on Forage - February 2025')
        st.write(
            '''
            - Completed a job simulation involving cybersecurity for PwC Digital Intelligence, gaining experience in understanding and explaining the concept of integrated defense.
            - Developed expertise in integrated defense strategies and their application in real-world scenarios.
            - Conducted risk assessments and formulated security recommendations for a client.
            - Demonstrated proficiency in cybersecurity terminology, network segmentation, and firewall configuration.
'''
        )


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




