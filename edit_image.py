import os
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
from diffusers.utils import load_image
from google_integrations import log_to_sheet
from PIL import Image

IMAGE_DIR = "generated_images"
MODEL_ID = "timbrooks/instruct-pix2pix"

def edit_image(image_path: str, edit_prompt: str) -> str:
    print(f"Applying edit '{edit_prompt}' to '{image_path}'")

    if not os.path.exists(image_path):
        return f"Error: The file '{image_path}' was not found."

    try:
        os.makedirs(IMAGE_DIR, exist_ok=True)

        pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
            MODEL_ID, torch_dtype=torch.float16, safety_checker=None
        )
        pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

        input_image = load_image(image_path).convert("RGB")

        edited_image = pipe(
            prompt=edit_prompt,
            image=input_image,
            num_inference_steps=10,
            image_guidance_scale=1
        ).images[0]

        edited_filename = f"edited_{os.path.basename(image_path)}"
        edited_file_path = os.path.join(IMAGE_DIR, edited_filename)
        
        edited_image.save(edited_file_path)
        print(f"Edited image saved to {edited_file_path}")

        log_values = [f"Edited: {os.path.basename(image_path)}", edit_prompt, edited_file_path]
        log_to_sheet(log_values)
        print(f"Logged edited image details to sheet.")

        return f"Success: Edited image saved locally at {edited_file_path}."

    except Exception as e:
        error_message = f"An unexpected error occurred in edit_image: {e}"
        print(error_message)
        return error_message

if __name__ == '__main__':
    pass
