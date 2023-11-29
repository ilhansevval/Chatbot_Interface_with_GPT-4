import streamlit as st

def about():
    with st.sidebar:
        col1, col2, = st.columns([1,2], gap="medium")
        with col1:
            st.image('docs/me.png', width=75)
        with col2:
            st.write(""" 
            Hey it's Şevval,
                     
            This is a Chatbot UI for OpenAI GPT-4.
                     
            It's written with less than 100 lines of code.
                    
            You'll need an OpenAI key to use this app, paste it below.
            """)

        col1, col2, col3, col4, col5, col6 = st.columns([1.1,1,1,1,1,1.5], gap="medium")
  
        with col2:
            # Medium
            medium_html = """
            <a href="https://medium.com/@ilhnsevval" target="_blank">
                <img src="https://www.svgrepo.com/show/445881/medium.svg" alt="Medium Logo" style="width:20px;">
            </a>
            """
            st.write(medium_html, unsafe_allow_html=True)       
        with col3:
            # Github
            github_html = """
            <a href="https://github.com/ilhansevval" target="_blank">
                <img src="https://www.svgrepo.com/show/506497/github.svg" alt="Medium Logo" style="width:25px;">
            </a>
            """
            st.write(github_html, unsafe_allow_html=True)
        with col4:
            # Linkedin
            linkedin_html = """
            <a href="https://www.linkedin.com/in/ilhansevval/" target="_blank">
                <img src="https://www.svgrepo.com/show/506517/linkedin.svg" alt="Medium Logo" style="width:25px;">
            </a>
            """
            st.write(linkedin_html, unsafe_allow_html=True)