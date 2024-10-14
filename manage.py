import os
import telebot
import requests

# Define your environment variables directly in the code
TELEGRAM_BOT_TOKEN = "7793448845:AAE9h_kvgaF5DXlTAqyyNYWGTUWEkBPZzfA"  # Your Telegram Bot Token
ZUKI_API_KEY = "zu-9d86e2ce1742e88bb2a4ebf7bedd4e7b"  # Your ZukiJourney API Key
# Initialize the bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Function to interact with ZukiJourney API (hypothetical example)
def generate_zuki_response(user_id, prompt):
    url = "https://api.zukijourney.com/v1/chat/completions"  # Hypothetical URL for ZukiJourney
    headers = {
        "Authorization": f"Bearer {ZUKI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",  # Change to the correct ZukiJourney model
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        assistant_message = response.json()['choices'][0]['message']['content']
        return assistant_message

    except Exception as e:
        print(f"ZukiJourney error: {e}")
        return "There was an issue with the jitendra ai. Please try again later."

# Handle Telegram messages and route to the ZukiJourney API
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    prompt = message.text.strip()

    # Route the request to ZukiJourney
    response = generate_zuki_response(user_id, prompt)
    bot.reply_to(message, response)

if __name__ == "__main__":
    print("Starting bot...")
    bot.polling()
