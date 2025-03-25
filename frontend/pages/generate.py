import streamlit as st
from core.blog_generator import BlogGeneratorSystem
from utils.llm_config import get_llm

def render_generate_page():
    st.title("Generate SEO-Optimized HR Blog")
    
    if 'blog_generator' not in st.session_state:
        st.session_state.blog_generator = BlogGeneratorSystem(get_llm())
    
    if st.button("Generate New Blog"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        def update_progress(message, value):
            status_text.text(message)
            progress_bar.progress(value)
        
        result = st.session_state.blog_generator.generate_blog(
            progress_callback=update_progress
        )
        
        if result["status"] == "success":
            st.success("Blog generated successfully!")
            
            st.subheader("Topic")
            st.write(result["metadata"]["topic"])
            
            st.subheader("Keywords")
            st.write(", ".join(result["metadata"]["keywords"]))
            
            st.subheader("Content")
            st.markdown(result["content"])
            
            # Add download button
            st.download_button(
                label="Download Blog",
                data=result["content"],
                file_name="blog_post.md",
                mime="text/markdown"
            )
        else:
            st.error(f"Error generating blog: {result['message']}")