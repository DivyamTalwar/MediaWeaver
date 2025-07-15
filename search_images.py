import requests
import os
from google_integrations import log_to_sheet

IMAGE_DIR = "generated_images"

def search_images(query: str, count: int = 3) -> str:
    api_key = os.environ.get("UNSPLASH_API_KEY")
    if not api_key:
        return "UNSPLASH_API_KEY is not set. Please set it in your environment."

    API_URL = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": count,
        "client_id": api_key,
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        
        results = response.json()["results"]
        if not results:
            return f"No images found for '{query}'. Please try a different query."
            
        saved_files = []
        for i, result in enumerate(results):
            image_url = result["urls"]["regular"]
            image_bytes = requests.get(image_url).content
            
            os.makedirs(IMAGE_DIR, exist_ok=True)
            filename = f"{query.replace(' ', '_')}_{i}.png"
            file_path = os.path.join(IMAGE_DIR, filename)
            
            with open(file_path, "wb") as f:
                f.write(image_bytes)
            
            saved_files.append(file_path)
            log_values = [f"Image Search: {query}", "Downloaded Image", file_path]
            log_to_sheet(log_values)
        
        return f"Success: {len(saved_files)} images saved in '{IMAGE_DIR}' and logged."

    except requests.exceptions.RequestException as e:
        return f"Error: Network or API request failed. {e}"
    except (IOError, KeyError) as e:
        return f"Error: Could not process API response. {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    pass
