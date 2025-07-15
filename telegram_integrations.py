import os
import telegram
import asyncio

async def send_telegram_message_async(message, chat_id):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        return "Error: TELEGRAM_BOT_TOKEN is not set."
        
    bot = telegram.Bot(token=bot_token)
    
    try:
        await bot.send_message(chat_id=chat_id, text=message)
        return "Success: Message sent to Telegram."
    except Exception as e:
        return f"Error sending message to Telegram: {e}"

async def send_telegram_photo_async(photo_path, caption, chat_id):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        return "Error: TELEGRAM_BOT_TOKEN is not set."
        
    bot = telegram.Bot(token=bot_token)
    
    try:
        with open(photo_path, 'rb') as photo_file:
            await bot.send_photo(chat_id=chat_id, photo=photo_file, caption=caption)
        return "Success: Photo sent to Telegram."
    except Exception as e:
        return f"Error sending photo to Telegram: {e}"

async def send_telegram_video_async(video_path, caption, chat_id):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        return "Error: TELEGRAM_BOT_TOKEN is not set."
    
    bot = telegram.Bot(token=bot_token)
    
    try:
        with open(video_path, 'rb') as video_file:
            await bot.send_video(chat_id=chat_id, video=video_file, caption=caption)
        return "Success: Video sent to Telegram."
    except Exception as e:
        return f"Error sending video to Telegram: {e}"

def send_telegram_message(message, chat_id, video_path=None):
    try:
        if video_path:
            asyncio.run(send_telegram_video_async(video_path, message, chat_id))
        else:
            asyncio.run(send_telegram_message_async(message, chat_id))
        return "Success: Message sent to Telegram."
    except Exception as e:
        return f"Error sending message to Telegram: {e}"

def send_telegram_photo(photo_path, caption, chat_id):
    try:
        asyncio.run(send_telegram_photo_async(photo_path, caption, chat_id))
        return "Success: Photo sent to Telegram."
    except Exception as e:
        return f"Error sending photo to Telegram: {e}"

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    
    CHAT_ID = "1403571279"
    pass
