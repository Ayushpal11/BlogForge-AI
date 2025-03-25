from langchain.prompts import PromptTemplate

RESEARCH_PROMPT = PromptTemplate(
    input_variables=["query"],
    template="Find current trending HR topics in 2024: {query}"
)

OUTLINE_PROMPT = PromptTemplate(
    input_variables=["topic", "research"],
    template="""
    Create a detailed blog outline for topic: {topic}
    Based on research: {research}
    Include:
    1. Introduction
    2. Main sections (at least 3)
    3. Subsections
    4. Conclusion
    """
)

CONTENT_PROMPT = PromptTemplate(
    input_variables=["outline", "research"],
    template="""
    Write a comprehensive 2000-word blog post following this outline:
    {outline}
    
    Use this research: {research}
    
    Ensure the content is:
    - Engaging and informative
    - Well-structured
    - Professional in tone
    - Includes relevant examples
    """
)

SEO_PROMPT = PromptTemplate(
    input_variables=["content", "keywords"],
    template="""
    Optimize this content for SEO using these keywords: {keywords}
    
    Content: {content}
    
    Ensure:
    - Proper keyword density
    - Meta description
    - Optimized headings
    - Internal linking opportunities
    """
)

REVIEW_PROMPT = PromptTemplate(
    input_variables=["content"],
    template="""
    Review and improve this content:
    {content}
    
    Check for:
    - Grammar and spelling
    - Clarity and coherence
    - Factual accuracy
    - Tone consistency
    """
)