from utils.llm_config import generate_response

class ContentPlanningAgent:
    def __init__(self, llm):
        self.llm = llm
        
    def create_outline(self, topic: str, research: str) -> dict:
        prompt = f"""
        Create a detailed blog outline for topic: {topic}
        Based on research: {research}
        Include:
        1. Introduction
        2. Main sections (at least 3)
        3. Subsections
        4. Conclusion
        """
        outline = generate_response(self.llm, prompt)
        
        return {"outline": outline}