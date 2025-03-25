from langchain_community.tools import DuckDuckGoSearchRun
from utils.llm_config import generate_response

class ResearchAgent:
    def __init__(self, llm):
        self.llm = llm
        self.search_tool = DuckDuckGoSearchRun()
        
    def find_trending_topics(self):
        search_results = self.search_tool.run("latest HR trends 2025 workplace")
        prompt = f"Find current trending HR topics in 2025 based on this research: {search_results}"
        trending_topics = generate_response(self.llm, prompt)
        
        return {
            "topics": trending_topics,
            "raw_research": search_results
        }