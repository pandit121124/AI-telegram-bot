

# How to Create and Deploy a Telegram Bot

### Steps Covered:
1. **Create a Telegram Bot**
2. **Set Up a Python Environment**
3. **Write Bot Code**
4. **Test Locally**
5. **Deploy to Heroku**
6. **Manage and Update Bot**

---

## 1. Create a Telegram Bot

To start building a bot, you'll need a bot token from Telegram.

### Steps:
1. **Open Telegram** and search for `@BotFather` (this is an official Telegram bot for managing bots).
2. **Start a conversation** with BotFather and type `/start`.
3. **Create a new bot** by typing `/newbot` and following the instructions.
4. **Bot Token**: After creating the bot, BotFather will provide a token. It will look something like this: `123456789:ABCDEF123456ghIkl-zyx57W2v1u123ew11`.

Save this token, as you'll need it to authenticate your bot with Telegram.

---

## 2. Set Up a Python Environment

### Prerequisites:
- **Python** installed (preferably Python 3.7+)
- **Pip** (Python package manager)
- **Git** (to push code to Heroku)

### Steps:
1. **Create a Project Folder**:
   ```bash
   mkdir my-telegram-bot
   cd my-telegram-bot
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**:
   Create a `requirements.txt` file to list the Python dependencies your bot will need. Use the following dependencies:

   ```bash
   pip install pyTelegramBotAPI requests
   ```

   Create `requirements.txt`:
   ```bash
   echo "pyTelegramBotAPI==4.23.0" > requirements.txt
   echo "requests==2.32.3" >> requirements.txt
   ```

---

## 3. Write Bot Code

Create a new Python file (e.g., `bot.py`) in your project folder to write your bot’s logic.

### Sample Code for `bot.py`:

```python
import os
import telebot
import requests

# Load the bot token from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Example of handling a simple /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot. How can I assist you?")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == "__main__":
    bot.polling()
```

This basic bot echoes back what the user says.

---

## 4. Test Locally

Before deploying, you should test your bot locally to ensure it's working properly.

### Steps:
1. **Set the Bot Token** in the environment:
   ```bash
   export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"  # On Windows: set TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   ```

2. **Run the Bot**:
   ```bash
   python bot.py
   ```

3. **Interact with Your Bot**: Open Telegram and send a message to your bot (use the name provided by BotFather).

---

## 5. Deploy the Bot to Heroku

To deploy your bot to Heroku, follow these steps.

### Prerequisites:
- **Heroku CLI**: Install from [Heroku’s official site](https://devcenter.heroku.com/articles/heroku-cli).

### Steps:

1. **Create a `Procfile`**:
   Heroku needs a `Procfile` to know how to run the app. Create a file named `Procfile` in your project folder with the following content:

   ```bash
   echo "worker: python bot.py" > Procfile
   ```

2. **Create a `.gitignore` File**:
   To prevent unnecessary files from being uploaded to Heroku, create a `.gitignore` file:

   ```bash
   echo "venv/" > .gitignore
   ```

3. **Initialize a Git Repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create a Heroku App**:
   ```bash
   heroku create your-heroku-app-name
   ```

5. **Set Environment Variables on Heroku**:
   You can set your bot token and other environment variables in Heroku like this:

   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   ```

6. **Push to Heroku**:
   Now you need to push your code to Heroku:

   ```bash
   git push heroku main  # Or git push heroku master if you don't have a 'main' branch
   ```

7. **Scale the Worker**:
   Your bot needs a worker to be active. Scale the worker process:

   ```bash
   heroku ps:scale worker=1
   ```

8. **Check Logs**:
   If there are any issues, you can check the Heroku logs:

   ```bash
   heroku logs --tail
   ```

---

## 6. Manage and Update the Bot

### Making Changes:
Whenever you need to update your bot code:

1. **Make Changes** in your Python files.
2. **Commit the Changes**:
   ```bash
   git add .
   git commit -m "Updated bot logic"
   ```

3. **Push the Changes to Heroku**:
   ```bash
   git push heroku main
   ```

4. **Check Logs** if Necessary:
   ```bash
   heroku logs --tail
   ```

---

## Additional Notes

- **Disabling Collectstatic**: If you're not using Django and Heroku fails on static collection, you can disable collectstatic:
  ```bash
  heroku config:set DISABLE_COLLECTSTATIC=1
  ```

- **Handling API Errors**: If you're integrating with external APIs (like ZukiJourney), ensure that you handle API errors gracefully in your bot.

- **Updating Requirements**: If you add new Python packages, don’t forget to update your `requirements.txt` by running:
  ```bash
  pip freeze > requirements.txt
  ```

---

### Useful Commands:

- **Heroku Logs**:
  ```bash
  heroku logs --tail
  ```

- **Scale Worker**:
  ```bash
  heroku ps:scale worker=1
  ```

- **Set Environment Variables**:
  ```bash
  heroku config:set TELEGRAM_BOT_TOKEN=your-telegram-bot-token
  ```

- **Stop Worker**:
  ```bash
  heroku ps:scale worker=0
  ```

