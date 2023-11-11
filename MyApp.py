import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image 



#intro title
st.set_page_config(page_title = "Aru Webpage", page_icon = ":pouting_cat:", layout = "wide")

#css link meow.css

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/meow.css")

#function to load animation ng Lottie pare!

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# assets to load lottiefile and other.
lottie_coding = load_lottieurl("https://lottie.host/e5920154-4601-4698-84dd-3cd4e5fd6a78/SLUl0GVzbY.json")
img_contact_form_1 = Image.open("images/1.png")
img_contact_form_2 = Image.open("images/3.png")
img_lottie_animation = Image.open("images/2.png")

#Header


with st.container():

    st.subheader ("Hi, I am Aldrich :skull:")
    st.title ("A Future Full Stack Developer")
    st.write ("My dream is to be a full Stack Developer and at the same time a Software Engineer.")
    st.write ("[Learn More >] (https://github.com/Arudrich)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Goal and Passion")
        st.write("##")
        st.write(
            """
            - Developing Websites with HTML / CSS
            - Learning Python
            - Want to learn how to build an App / Website using React
            - Working to be better Programmer and Engineer

            If this sounds interesting to you, contact me in my email or in any of my social media.
            """
        )
        st.write("[Instragram >](https://www.instagram.com/arudrich_/?hl=en)")
        st.write("[Facebook >](https://www.facebook.com/Arudrich)")

    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

# list of my projects 11 / 09 / 23
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Simple Face Detection Using PYTHON")
        st.write(
            """
            This program is use to detect the frontal face of a person with the use of python programming
            """
        )
        st.markdown("[Github Link...](https://github.com/Arudrich/Simple-Face-Detection)")
    st.write("##")
    st.write("##")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form_1)
    with text_column:
        st.subheader("Basic Portfolio of Mine Using HTML and CSS")
        st.write(
            """
            This is my simple Portfolio that I made using HTML and CSS.
            This is just a basic coding but I am very proud of it!
            """
        )
        st.markdown("[Github Link...](https://github.com/Arudrich/Simple-Sample-Portfolio)")
    st.write("##")
    st.write("##")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form_2)
    with text_column:
        st.subheader("Streamlit Python Basic Website")
        st.write(
            """
            This is the Github link of this Actual Website!
            """
        )
        st.markdown("[Github Link...](https://github.com/Arudrich/Simple-Sample-Portfolio)")

        
# CONTACT SECTION TO!
with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/aldrichdmacadangdang11@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
