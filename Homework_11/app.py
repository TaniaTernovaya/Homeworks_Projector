from urllib import parse, request
import json
from aiogram import Bot, Dispatcher, executor, types
from data import config

bot = Bot(token=config.BOT_TOKEN)  # створююю змінну бота
dp = Dispatcher(bot=bot)  # створюю диспетчера


# створююю хендлера, що відповідає на перше повідомлення
@dp.message_handler(commands=["start"])
async def start_bot(
    message: types.Message,
):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await message.reply(f"Hello, {user_name}. What are you looking for?")


# створююю хендлера, що відповідає на всі повідомлення юзера: шукає гіфку до слова і видає картинку з відповідним контентом
@dp.message_handler()
async def get_result(message: types.Message):
    URL = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode(
        {
            "q": {message.text},
            "api_key": "vmvjD9CwhpEtXwstukeijPNtk10owJkc",
            "limit": "1",
        }
    )
    try:
        with request.urlopen("".join((URL, "?", params))) as response:
            data = json.loads(response.read())
            json_data = json.dumps(data, sort_keys=True, indent=4)
            json_dict = json.loads(json_data)
            for data in json_dict:
                data = json_dict["data"]
            result = data[0]["images"]["original"]["url"]
        await message.reply_animation(result)
    except IndexError:
        await message.reply("Something went wrong")


if __name__ == "__main__":
    executor.start_polling(dp)
