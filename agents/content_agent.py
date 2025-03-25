from utils.llm_config import generate_response

class ContentGenerationAgent:
    def __init__(self, llm):
        self.llm = llm
        
    def generate_content(self, outline: str, research: str) -> str:
        prompt = f"""
        Write a comprehensive 2000-word blog post following this outline:
        {outline}
        
        Use this research: {research}
        
        Ensure the content is:
        - Engaging and informative
        - Well-structured
        - Professional in tone
        - Includes relevant examples
        """
        return generate_response(self.llm, prompt)