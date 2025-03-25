import streamlit as st

# Must be the first Streamlit command
st.set_page_config(
    page_title="HR Blog Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

from frontend.pages.generate import render_generate_page
from frontend.components.sidebar import render_sidebar
from frontend.pages.home import render_home_page

def main():
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    render_sidebar()

    # Render the appropriate page
    if st.session_state.page == "generate":
        render_generate_page()
    else:
        render_home_page()

if __name__ == "__main__":
    main()