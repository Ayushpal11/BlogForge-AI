# import streamlit as st

# def render_sidebar():
#     # Expanded custom CSS for sidebar styling
#     st.markdown("""
#     <style>
#     /* Sidebar Container Styling */
#     .sidebar .sidebar-content {
#         background: linear-gradient(to bottom, #f0f2f6, #e9edf3);
#         color: #2c3e50;
#         border-right: 2px solid #d0d6e0;
#         box-shadow: 2px 0 5px rgba(0,0,0,0.05);
#     }

#     /* Sidebar Title Styling */
#     .sidebar-title {
#         color: #2c3e50;
#         font-weight: bold;
#         text-align: center;
#         padding-bottom: 15px;
#         border-bottom: 3px solid #3498db;
#         margin-bottom: 20px;
#         font-size: 1.5em;
#     }

#     /* Navigation Buttons Styling */
#     .stButton>button {
#         width: 100%;
#         text-align: left;
#         justify-content: flex-start;
#         background-color: #ffffff;
#         border: 1px solid #e0e4e8;
#         color: #2c3e50;
#         margin-bottom: 10px;
#         padding: 10px 15px;
#         border-radius: 8px;
#         transition: all 0.3s ease;
#         display: flex;
#         align-items: center;
#         gap: 10px;
#     }
#     .stButton>button:hover {
#         background-color: #3498db;
#         color: white;
#         border-color: #3498db;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         transform: translateY(-2px);
#     }
#     .stButton>button:active {
#         background-color: #2980b9;
#         color: white;
#         transform: translateY(0);
#     }

#     /* Sections Spacing */
#     .nav-section, .settings-section {
#         margin-top: 20px;
#     }

#     /* Slider and Selectbox Styling */
#     .stSlider, .stSelectbox {
#         margin-bottom: 15px;
#     }

#     /* Footer Styling */
#     .sidebar-footer {
#         text-align: center;
#         color: #7f8c8d;
#         font-size: 0.8em;
#         margin-top: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Sidebar content
#     with st.sidebar:
#         # Title with custom styling
#         st.markdown('<h1 class="sidebar-title">HR Blog Generator</h1>', unsafe_allow_html=True)
        
#         # Navigation Section
#         st.markdown('<div class="nav-section">', unsafe_allow_html=True)
#         st.markdown("### Navigation")
        
#         # Navigation buttons with improved layout
#         nav_cols = st.columns(2)
        
#         with nav_cols[0]:
#             if st.button("🏠 Home", key="home_btn"):
#                 st.session_state.page = "home"
        
#         with nav_cols[1]:
#             if st.button("✍️ Generate", key="generate_btn"):
#                 st.session_state.page = "generate"
        
#         st.markdown('</div>', unsafe_allow_html=True)
        
#         # Divider
#         st.markdown("---")
        
#         # Settings Section
#         st.markdown('<div class="settings-section">', unsafe_allow_html=True)
#         st.markdown("### Blog Generation Settings")
        
#         # Content Length Slider with enhanced styling
#         st.session_state.content_length = st.slider(
#             "Content Length (words)", 
#             min_value=500, 
#             max_value=3000, 
#             value=2000,
#             help="Select the desired word count for your blog post"
#         )
        
#         # Writing Style Selector with enhanced styling
#         st.session_state.writing_style = st.selectbox(
#             "Writing Style", 
#             ["Professional", "Casual", "Technical"],
#             help="Choose the tone and style of your blog post"
#         )
#         # Divider
#         st.markdown("---")
#         # Footer
#         st.markdown('<div class="sidebar-footer">*Powered by Mistral AI*</div>', unsafe_allow_html=True)

# # Initialize session state for page tracking and settings
# def initialize_session_state():
#     default_states = {
#         'page': 'home',
#         'content_length': 2000,
#         'writing_style': 'Professional',
#         'use_ai_suggestions': False,
#         'include_trends': False
#     }
    
#     for key, value in default_states.items():
#         if key not in st.session_state:
#             st.session_state[key] = value

# # Call initialization and sidebar rendering
# initialize_session_state()
# render_sidebar()


import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown('<h1 class="sidebar-title">HR Blog Generator</h1>', unsafe_allow_html=True)
        st.markdown("---")
        # Navigation Section
        st.markdown('<div class="nav-section">', unsafe_allow_html=True)
        st.markdown("### Navigation")
        
        # Navigation buttons with improved layout
        nav_cols = st.columns(2)
        
        with nav_cols[0]:
            if st.button("🏠 Home", key="home_btn"):
                st.session_state.page = "home"
        
        with nav_cols[1]:
            if st.button("✍️ Generate", key="generate_btn"):
                st.session_state.page = "generate"
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        # Settings
        with st.expander("⚙️ Settings"):
            st.selectbox(
                "Language",
                ["English", "Spanish", "French"],
                key="sidebar_setting_language"
            )
            
            st.select_slider(
                "Writing Style",
                options=["Casual", "Balanced", "Professional"],
                value="Balanced",
                key="sidebar_setting_style"
            )
            
            st.slider(
                "Content Length",
                1000,
                3000,
                2000,
                100,
                key="sidebar_setting_length"
            )
        st.markdown("---")
        # About section
        with st.expander("ℹ️ About"):
            st.markdown("""
            ### HR Blog Generator v1.0
            
            An AI-powered tool for generating professional HR blog content.
            
            Made with ❤️ using Streamlit and Mistral AI
            """)