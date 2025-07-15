from ddgs import DDGS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from google_integrations import log_to_sheet

def get_news(topic: str) -> str:
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.news(f"latest news on {topic}", max_results=5)]
        
        if not results:
            return f"No news found for '{topic}'. Please try a different topic."
            
        news_context = "\n\n".join([f"Title: {r['title']}\nBody: {r['body']}\nSource: {r['url']}" for r in results])

        prompt = f"""
        You are a senior news analyst. Your task is to synthesize the latest news articles on the topic of '{topic}' into a single, comprehensive, and insightful summary.

        **Instructions:**
        1.  **Analyze the Context:** Carefully review the following news articles.
            <news_articles>
            {news_context}
            </news_articles>
        2.  **Identify Key Themes:** Identify the 2-3 most important themes or developments from the articles.
        3.  **Write a Coherent Summary:**
            *   Start with a strong opening sentence that summarizes the current situation.
            *   Dedicate a paragraph to each key theme, explaining it clearly and providing context.
            *   Do not simply list the news. Weave the information into a single, well-written narrative.
            *   Maintain a neutral, objective, and professional tone.
        4.  **Conclusion:** Conclude with a brief outlook on what might happen next regarding this topic.

        **Output Format:**
        - The entire output should be a single block of text.
        """

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        response = llm.invoke([HumanMessage(content=prompt)])
        news_summary = response.content
        
        log_values = [f"News Search: {topic}", "Generated Summary", "N/A"]
        log_to_sheet(log_values)
        
        return news_summary

    except Exception as e:
        return f"An unexpected error occurred while searching for news: {e}"

if __name__ == '__main__':
    pass
