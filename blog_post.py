import os
from ddgs import DDGS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from google_integrations import log_to_sheet

BLOG_DIR = "generated_blogs"

def blog_post(topic: str, audience: str) -> str:
    print(f"BLOG POST: Generating post for topic '{topic}' for audience '{audience}'")

    try:
        os.makedirs(BLOG_DIR, exist_ok=True)

        with DDGS() as ddgs:
            search_results = [r for r in ddgs.news(f"latest trends in {topic} for {audience}", max_results=5)]
        
        search_context = "\n".join([f"- {res['title']}: {res['body']}" for res in search_results])

        prompt = f"""
        You are a world-class content creator and SEO expert. Your task is to write a detailed, engaging, and comprehensive blog post on the topic of '{topic}' tailored for an audience of '{audience}'.

        **Instructions:**
        1.  **Title:** Create a compelling and SEO-friendly title for the blog post.
        2.  **Introduction:** Start with a strong hook to grab the reader's attention. Clearly state the purpose of the post and what the reader will learn.
        3.  **Main Body:**
            *   Create at least 3-5 detailed sections, each with a clear heading (use Markdown H2 or H3).
            *   Incorporate the latest trends and information. Use the following search results as context and inspiration, but do not simply copy them. Expand on these points with your own expert insights.
                <search_results>
                {search_context}
                </search_results>
            *   Use bullet points, bold text, and other formatting to make the content easy to read and digest.
            *   Maintain a professional, authoritative, yet approachable tone.
        4.  **Conclusion:** Summarize the key takeaways from the post.
        5.  **Call to Action (CTA):** End with a clear call to action. This could be asking a question to encourage comments, suggesting readers share the post, or pointing them to another resource.

        **Output Format:**
        - The entire output must be in Markdown format.
        - Ensure the blog post is at least 800 words long.
        """

        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        response = llm.invoke([HumanMessage(content=prompt)])
        generated_post = response.content
        
        filename = f"{topic.replace(' ', '_')}_{audience.replace(' ', '_')}.md"
        file_path = os.path.join(BLOG_DIR, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generated_post)
            
        log_values = [f"Blog: {topic}", f"Audience: {audience}", file_path]
        log_to_sheet(log_values)
        
        return f"Success: Blog post created and saved locally at {file_path}"

    except Exception as e:
        error_message = f"An unexpected error occurred in blog_post: {e}"
        return error_message

if __name__ == '__main__':
    pass
