import os
import requests
from PIL import Image
from io import BytesIO
from google_integrations import log_to_sheet
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

IMAGE_DIR = "generated_images"
HF_IMAGE_GEN_MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

def create_image(image_prompt: str, title: str) -> str:
    print(f"Generating image for prompt '{image_prompt}' with title '{title}'")

    try:
        os.makedirs(IMAGE_DIR, exist_ok=True)

        llm = HuggingFaceEndpoint(
            endpoint_url=HF_IMAGE_GEN_MODEL,
            task="text-to-image",
            max_new_tokens=512,
            top_k=50,
            top_p=0.95,
            typical_p=0.95,
            temperature=0.8,
            repetition_penalty=1.03,
        )
        
        image_bytes = llm.invoke(image_prompt)
        
        image = Image.open(BytesIO(image_bytes))
        
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
