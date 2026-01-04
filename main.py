import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

# Bot tokeningizni bitta joyga yozib qo'yamiz
API_TOKEN = '7532712344:AAEn-sttm7oaKtqLypaSb7ZINPvPyi5H2P8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # PASTDAGI LINKNI O'ZINGIZNING GITHUB PAGES LINKINGIZGA ALMASHTIRING
    web_app = WebAppInfo(url="https://husanboy832.github.io/shuxrat-cinema-app/")
    
    markup.add(types.KeyboardButton("Xizmatlarni ko'rish ✨", web_app=web_app))
    
    await message.answer(
        f"Assalomu alaykum, {message.from_user.full_name}!\n"
        "**SHUXRAT CINEMA** studiyasining rasmiy botiga xush kelibsiz.\n"
        "Xizmatlarimiz bilan tanishish uchun pastdagi tugmani bosing.",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@dp.message_handler(content_types=['web_app_data'])
async def web_app_data_handler(message: types.Message):
    # Bu qism mijoz tugmani bosganda sizga xabar yuboradi
    data = message.web_app_data.data
    await message.answer(f"Raxmat! Siz quyidagini tanladingiz: {data}\nTez orada siz bilan bog'lanamiz! ✅")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

