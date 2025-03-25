import streamlit as st

def render_home_page():
    # Custom CSS for styling
    st.markdown("""
    <style>
    .home-container {
        background-color: #f0f4f8;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    .welcome-header {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .feature-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
    }
    .feature-icon {
        font-size: 2.5rem;
        color: #3498db;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    
    # Welcome Header
    st.markdown('<h1 class="welcome-header">🤖 HR Blog Generator</h1>', unsafe_allow_html=True)
    
    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        # Features Section
        st.markdown("### 🚀 Key Features")
        
        # Feature Cards
        features = [
            {
            "icon": "✍️",
            "title": "AI-Powered Writing",
            "description": "Generate high-quality HR blog posts instantly with advanced AI technology."
            },
            {
            "icon": "🎨",
            "title": "Customizable Styles",
            "description": "Choose from professional, casual, or technical writing tones to match your brand."
            }
        ]
        
        for feature in features:
            st.markdown(f'''
            <div class="feature-card">
            <div style="display: flex; align-items: relative;">
                <div class="feature-icon" style="margin-right: 15px;">{feature["icon"]}</div>
                <div>
                <h3 style="color: #2c3e50; margin: 0;">{feature["title"]}</h3>
                <p style="color: #2c3e50; margin: 5px 0 0 0;">{feature["description"]}</p>
                </div>
            </div>
            </div>
            ''', unsafe_allow_html=True)
        

        # Quick Start Guide
        st.markdown("### 🚀 Quick Start Guide")
        steps = [
            "Select your desired writing style",
            "Choose content length",
            "Click 'Generate' to create your blog post",
            "Review and refine the generated content"
        ]
        
        for i, step in enumerate(steps, 1):
            st.markdown(f"**Step {i}:** {step}")

    st.markdown("</div>", unsafe_allow_html=True)

def main():
    render_home_page()

if __name__ == "__main__":
    main()