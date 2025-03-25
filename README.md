# BlogForge AI 🤖📝

## Overview

BlogForge AI is an innovative Multi Agent Streamlit-based application that leverages AI to create high-quality, professional HR-related blog posts with ease. This tool empowers HR professionals and content creators to generate engaging, insightful blog content quickly and efficiently.

## 🌟 Features

### AI-Powered Content Generation
- Generate professional HR blog posts instantly
- Customizable writing styles
- Flexible content length control

### Key Capabilities
- Multiple writing tone options
- Word count customization
- User-friendly interface
- Easy blog content creation

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python Package Manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/hr-blog-generator.git
cd hr-blog-generator
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## 🔧 Project Structure
```
├── agents/                 # AI agents for different tasks
│   ├── research_agent.py
│   ├── planning_agent.py
│   ├── content_agent.py
│   ├── seo_agent.py
│   └── review_agent.py
├── utils/                  # Utility functions
│   ├── llm_config.py
│   └── prompts.py
├── core/                   # Core logic
│   └── blog_generator.py
├── frontend/              # Streamlit UI components
│   ├── pages/
│   │   ├── home.py
│   │   └── generate.py
│   │  
│   └── components/
│       └── sidebar.py
├── samples/                # Blog Samples that were created by BlogForge AI 
|   ├── blog_post.md 
|   └── blog_post(1).md
├── app.py                 # Main file
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation


## 🖥️ Running the Application

```bash
streamlit run app.py
```

## 🛠️ Customization

### Writing Styles
- Professional
- Casual
- Technical

### Content Length
- Adjustable from 500 to 3000 words

## 📦 Dependencies
- Streamlit
- LangChain
- Mistral AI

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
