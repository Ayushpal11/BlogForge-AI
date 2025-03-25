from utils.llm_config import generate_response
from typing import List

class SEOOptimizationAgent:
    def __init__(self, llm):
        self.llm = llm
        
    def optimize_content(self, content: str, target_keywords: List[str]) -> str:
        prompt = f"""
        Optimize this content for SEO using these keywords: {', '.join(target_keywords)}
        
        Content: {content}
        
        Ensure:
        - Proper keyword density
        - Meta description
        - Optimized headings
        - Internal linking opportunities
        """
        return generate_response(self.llm, prompt)