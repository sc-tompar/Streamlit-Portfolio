import streamlit as st
from PIL import Image

st.markdown("""
<style>
body {
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #FAFAFA;
    color: #333333;
    padding: 5px;
}
h1 {
    color: #0068C9;
    text-align: center;
}
h2 {
    color: #333333;
    font-weight: bold;
}
img {
    margin: 0 auto;
    display: block;
}
div.row-widget.stRadio > div {
    flex-direction: row;
}
.css-1siy2j7 {
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}
.css-1aumxhk {
    background-color: #f1f3f5;
    border-radius: 10px;
    padding: 10px;
}
.css-1d391kg {
    padding-top: 0;
    padding-bottom: 0;
}
</style>
""", unsafe_allow_html=True)

st.title("Simoun Tompar's Portfolio")

image = Image.open('image1.jpg')  
st.image(image, caption='Simoun Tompar', width=100, use_column_width=True)  

st.sidebar.title('Portfolio Sections')
page = st.sidebar.radio('Go to', ['Biography', 'Education', 'Skills', 'Certifications', 'Contact'])

if page == 'Biography':
    st.subheader("Biography")
    st.write("""
    Aspiring web and front-end developer from Cebu City, Philippines, currently completing my Bachelor of 
    Science in Information Technology at Cebu Institute of Technology-University. With a strong foundation 
    in Python and Django, I am passionate about leveraging web technologies and software development to 
    build dynamic solutions.
    """)

elif page == 'Education':
    st.subheader("Education")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**University of San Jose – Recoletos**")
        st.write("Senior High School - STEM, With honors")
    with col2:
        st.write("2020-2021")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("**Cebu Institute of Technology - University**")
        st.write("Bachelor of Science in Information Technology")
    with col2:
        st.write("Present")

elif page == 'Skills':
    st.subheader("Technical Skills")
    st.write("""
    - **Programming Languages**: HTML, CSS, C, Java, JavaScript, PHP, Python
    - **Frameworks**: Django, Flask, Spring, React, Streamlit
    - **Tools**: MS Office, Outlook, Canva, GitHub, Figma, DrawIO, Filmora X
    - **Languages**: Cebuano, English, Filipino
    """)

    st.subheader("Additional Skills")
    st.write("""
    - Effective time management and communicator.
    - Creative problem-solving skills.
    - Quick learner with a passion for technology.
    - Able to work collaboratively in teams or independently.
    """)

elif page == 'Certifications':
    st.subheader("Certifications")
    st.write("""
    - Huawei Talent Online – HCIP Storage Expert Course
    - Kaggle – Data Visualization Online Course
    - Alison – Data Analytics Online Course
    - British Council English Score – B2 Core Skills Test
    - RSPETH's Virtual Learning Session
    - Participation – Cebu ICT Student Congress
    """)

elif page == 'Contact':
    st.subheader("Contact Information")
    st.write("📧 Primary: sc.tompar@gmail.com")
    st.write("📧 Secondary: simouncloyd.tompar@cit.edu")
    st.write("📞 Phone: 09183643605")

st.markdown("---")
st.write("Thank you for visiting my creative portfolio. Feel free to connect!")
