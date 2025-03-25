from utils.llm_config import generate_response

class ReviewAgent:
    def __init__(self, llm):
        self.llm = llm
        
    def review_content(self, content: str) -> str:
        prompt = f"""
        Review and improve this content:
        {content}
        
        Check for:
        - Grammar and spelling
        - Clarity and coherence
        - Factual accuracy
        - Tone consistency
        """
        return generate_response(self.llm, prompt)