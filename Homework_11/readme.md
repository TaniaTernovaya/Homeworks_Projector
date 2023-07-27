# ![Bot](logo.png=40x40) Telegram Bot - "GetGif"

This is a simple Telegram bot that allows users to find GIFs related to specific words using the Giphy API. When a user sends a word to the bot, it will respond with a relevant GIF fetched from the https://giphy.com.

## How to Use

1. **Start the Bot:** You can start using the bot by searching for it on Telegram [link](t.me/testternovaya_bot) and sending the command `/start`. The bot will then send a welcome message and be ready to receive your search queries.
2. **Send a Word:** To get a GIF, simply type a word and send it to the bot as a message. The bot will then fetch a related GIF from Giphy and reply to you with the result.
3. **Keep it Family-Friendly:** Please remember to use appropriate and family-friendly words when interacting with the bot.

## Running the Bot

To run this bot on your own server or machine, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:

git clone https://github.com/yourusername/your-repo-name.git

2. **Install Dependencies:** Navigate to the project directory and install the required dependencies:
cd your-repo-name
pip install -r requirements.txt

3. **Create a Telegram Bot:** To create your own Telegram bot, follow the official [Telegram Bot documentation](https://core.telegram.org/bots#3-how-do-i-create-a-bot). Note down the API token you receive after creating the bot.

4. **Get Giphy API Key:** To use the Giphy API, you'll need an API key. You can obtain one by signing up on the [Giphy Developers](https://developers.giphy.com/) website.

5. **Configure API Keys:** Open the `data/conf