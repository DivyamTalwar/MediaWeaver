import os
import requests
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from google_integrations import log_to_sheet
from langchain_google_genai import ChatGoogleGenerativeAI

VIDEO_DIR = "generated_videos"
IMAGE_DIR = "generated_images"
AUDIO_DIR = "generated_audio" 
UNSPLASH_API_KEY = os.environ.get("UNSPLASH_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

def generate_script(topic: str) -> str:
    print(f"Generating script for '{topic}'")
    prompt = f"""
    You are a professional scriptwriter tasked with creating a short, engaging, and informative video script on the topic: '{topic}'.

    **Instructions:**
    1.  **Hook:** Start with a compelling question or a surprising fact to capture the viewer's attention within the first 3 seconds.
    2.  **Body:**
        *   Tell a concise story or explain the core concepts clearly.
        *   Break down the information into 2-3 key points.
        *   Use simple, conversational language that is easy to understand.
    3.  **Conclusion:** End with a memorable summary or a thought-provoking statement.
    4.  **Word Count:** The script should be approximately 150-200 words to fit a short video format.
    5.  **Output:** Provide the script as a single, continuous block of text without any headings or special formatting.
    """
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        print(f"ERROR in script generation: {e}")
        return f"An error occurred while generating the script for {topic}."

def search_unsplash_images(query: str, count: int = 5):
    print(f"Searching for '{query}'")
    headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
    params = {"query": query, "per_page": count, "orientation": "landscape"}
    response = requests.get("https://api.unsplash.com/search/photos", headers=headers, params=params)
    if response.status_code == 200:
        results = response.json()["results"]
        return [res["urls"]["regular"] for res in results]
    else:
        print(f"ERROR fetching from Unsplash: {response.status_code} - {response.text}")
        return []

def download_image(url: str, folder: str, filename: str) -> str:
    path = os.path.join(folder, filename)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return path
    return None

def faceless_video(topic: str) -> str:
    print(f"FACELESS VIDEO: Starting process for topic '{topic}'")
    try:
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(IMAGE_DIR, exist_ok=True)
        os.makedirs(AUDIO_DIR, exist_ok=True)

        script = generate_script(topic)
        if "error occurred" in script:
            raise Exception(script)

        audio_filename = f"{topic.replace(' ', '_')}.mp3"
        audio_path = os.path.join(AUDIO_DIR, audio_filename)
        tts = gTTS(text=script, lang='en')
        tts.save(audio_path)
        print(f"TTS: Audio saved to {audio_path}")

        image_urls = search_unsplash_images(topic, count=5)
        if not image_urls:
            raise Exception("Could not find any images for the topic.")
        
        image_paths = []
        for i, url in enumerate(image_urls):
            img_path = download_image(url, IMAGE_DIR, f"temp_{i}.jpg")
            if img_path:
                image_paths.append(img_path)
        
        if not image_paths:
            raise Exception("Failed to download images.")

        audio_clip = AudioFileClip(audio_path)
        clip_duration = audio_clip.duration / len(image_paths)
        
        video_clips = [ImageClip(path).set_duration(clip_duration) for path in image_paths]
        final_clip = concatenate_videoclips(video_clips, method="compose")
        final_clip = final_clip.set_audio(audio_clip)

        video_filename = f"{topic.replace(' ', '_')}.mp4"
        video_path = os.path.join(VIDEO_DIR, video_filename)
        final_clip.write_videofile(video_path, fps=24, codec='libx264')
        print(f"Video saved to {video_path}")

        log_values = [f"Video: {topic}", "Generated Video", video_path]
        log_to_sheet(log_values)
        print(f"Logged video details to sheet.")

        for path in image_paths:
            os.remove(path)
        os.remove(audio_path)

        return f"Success: Video created and saved locally at {video_path}."

    except Exception as e:
        error_message = f"An unexpected error occurred in faceless_video: {e}"
        print(error_message)
        return error_message

if __name__ == '__main__':
    pass
