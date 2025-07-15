import os
import json
from google_integrations import log_to_sheet
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

def content_strategist(topic: str) -> str:
    print(f"CONTENT STRATEGIST: Generating strategy for '{topic}'")
    
    prompt = f"""
    You are a world-class content strategist and creative director. Your task is to generate a comprehensive and highly detailed content plan for the topic: "{topic}".

    Your plan must be a valid JSON object with the following keys:
    - "blog_post_title": Create a highly compelling, SEO-optimized title that is irresistible to click. It should promise significant value and insight.
    - "linkedin_post_hook": Write a powerful, attention-grabbing hook for a LinkedIn post. It should be a bold statement, a surprising statistic, or a provocative question that stops the scroll.
    - "faceless_video_script_idea": Outline a concept for a short, engaging faceless video (under 60 seconds). Describe the narrative, the key message, and the overall tone.
    - "image_prompts": Generate a list of three distinct, highly detailed, and visually stunning prompts for an AI image generator. Each prompt should describe a complete scene with specific details about the subject, setting, lighting, and style. For example, instead of "a robot," write "a hyper-realistic, chrome-plated humanoid robot examining a glowing plant in a futuristic, neon-lit laboratory."

    Ensure the output is ONLY the JSON object, with no extra text or markdown formatting.
    """

    try:
        response = llm.invoke(prompt)
        generated_text = response.content.strip()

        cleaned_content = generated_text.replace("```json", "").replace("```", "").strip()
        
        content = json.loads(cleaned_content)
        
        log_values = [f"Content Strategy: {topic}", "Generated Plan", json.dumps(content)]
        log_to_sheet(log_values)
        
        return json.dumps(content)

    except json.JSONDecodeError as e:
        error_msg = f"Error decoding JSON from model response: {e}. Raw response: {generated_text}"
        print(error_msg)
        return json.dumps({"error": error_msg})
    except Exception as e:
        error_msg = f"An unexpected error occurred in content_strategist: {e}"
        print(error_msg)
        return json.dumps({"error": error_msg})

if __name__ == '__main__':
    pass
