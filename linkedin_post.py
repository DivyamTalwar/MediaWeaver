import os
from ddgs import DDGS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from google_integrations import log_to_sheet

LINKEDIN_DIR = "generated_linkedin_posts"

def linkedin_post(topic: str, audience: str) -> str:
    print(f"Generating post for topic '{topic}' for audience '{audience}'")

    try:
        os.makedirs(LINKEDIN_DIR, exist_ok=True)

        with DDGS() as ddgs:
            search_results = [r for r in ddgs.news(f"latest news and insights on {topic} for {audience}", max_results=3)]
        
        search_context = "\n".join([f"- {res['title']}: {res['body']}" for res in search_results])

        prompt = f"""
        You are a world-class social media manager and content strategist, specializing in LinkedIn. Your task is to create a compelling and professional LinkedIn post on the topic of '{topic}' for an audience of '{audience}'.

        **Instructions:**
        1.  **Hook:** Start with a powerful opening that grabs attention immediately. This could be a surprising statistic, a bold statement, or a relatable question.
        2.  **Body:**
            *   Provide valuable insights and key takeaways.
            *   Structure the body with 2-3 short paragraphs or a bulleted list for readability.
            *   Incorporate insights from the latest news and trends. Use the following search results as context, but rephrase and expand upon them with your expert perspective.
                <search_results>
                {search_context}
                </search_results>
            *   Maintain a professional and authoritative tone suitable for LinkedIn.
        3.  **Call to Action (CTA):** End with a question to encourage engagement and discussion in the comments.
        4.  **Hashtags:** Include 3-5 relevant and strategic hashtags to increase visibility. Do not use generic hashtags.

        **Output Format:**
        - The entire output must be a single block of text, ready to be copied and pasted.
        - The post should be concise, ideally between 150-250 words.
        """

        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        response = llm.invoke([HumanMessage(content=prompt)])
        generated_post = response.content
        
        filename = f"{topic.replace(' ', '_')}_{audience.replace(' ', '_')}.txt"
        file_path = os.path.join(LINKEDIN_DIR, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generated_post)
            
        log_values = [f"LinkedIn: {topic}", f"Audience: {audience}", file_path]
        log_to_sheet(log_values)
        
        return f"Success: LinkedIn post created and saved locally at {file_path}"

    except Exception as e:
        error_message = f"An unexpected error occurred in linkedin_post: {e}"
        return error_message

if __name__ == '__main__':
    pass
