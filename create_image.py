import os
from PIL import Image
from google_integrations import log_to_sheet
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

IMAGE_DIR = "generated_images"
HF_IMAGE_GEN_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

def create_image(image_prompt: str, title: str) -> str:
    print(f"Generating image for prompt '{image_prompt}' with title '{title}'")

    try:
        os.makedirs(IMAGE_DIR, exist_ok=True)

        if not HF_API_TOKEN:
            raise ValueError("Hugging Face API token not found. Please set the HF_API_TOKEN environment variable.")

        client = InferenceClient(token=HF_API_TOKEN)
        
        image = client.text_to_image(image_prompt, model=HF_IMAGE_GEN_MODEL)
        
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '_')).rstrip()
        filename = f"{safe_title.replace(' ', '_')}.png"
        file_path = os.path.join(IMAGE_DIR, filename)
        
        image.save(file_path)
        print(f"Image saved to {file_path}")

        log_values = [title, image_prompt, file_path]
        log_to_sheet(log_values)
        print(f"Logged image details to sheet.")

        return f"Image created and saved locally at {file_path}."

    except Exception as e:
        error_message = f"An unexpected error occurred in create_image: {e}"
        print(error_message)
        return error_message

if __name__ == '__main__':
    pass
