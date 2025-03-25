from agents.research_agent import ResearchAgent
from agents.planning_agent import ContentPlanningAgent
from agents.content_agent import ContentGenerationAgent
from agents.seo_agent import SEOOptimizationAgent
from agents.review_agent import ReviewAgent

class BlogGeneratorSystem:
    def __init__(self, llm):
        self.llm = llm
        self.research_agent = ResearchAgent(self.llm)
        self.planning_agent = ContentPlanningAgent(self.llm)
        self.content_agent = ContentGenerationAgent(self.llm)
        self.seo_agent = SEOOptimizationAgent(self.llm)
        self.review_agent = ReviewAgent(self.llm)
    
    def generate_blog(self, progress_callback=None):
        try:
            if progress_callback:
                progress_callback("Researching topics...", 0.2)
            research_results = self.research_agent.find_trending_topics()
            
            if progress_callback:
                progress_callback("Creating outline...", 0.4)
            outline_results = self.planning_agent.create_outline(
                research_results["topics"],
                research_results["raw_research"]
            )
            
            if progress_callback:
                progress_callback("Generating content...", 0.6)
            content = self.content_agent.generate_content(
                outline_results["outline"],
                research_results["raw_research"]
            )
            
            if progress_callback:
                progress_callback("Optimizing for SEO...", 0.8)
            keywords = ["HR trends", "workplace", "employee management"]
            optimized_content = self.seo_agent.optimize_content(content, keywords)
            
            if progress_callback:
                progress_callback("Reviewing content...", 0.9)
            final_content = self.review_agent.review_content(optimized_content)
            
            if progress_callback:
                progress_callback("Done!", 1.0)
            
            return {
                "status": "success",
                "content": final_content,
                "metadata": {
                    "topic": research_results["topics"],
                    "keywords": keywords,
                    "outline": outline_results["outline"]
                }
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }