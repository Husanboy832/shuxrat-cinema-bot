import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from fpdf import FPDF
import os

# --- SOZLAMALAR ---
TOKEN = "7532712344:AAEn-sttm7oaKtqLypaSb7ZINPvPyi5H2P8" # @BotFather dan olgan kod
ADMINS = [8019349816] # O'zingizning ID raqamingizni yozing
MINI_APP_URL = "https://google.com" # Hozircha Google, keyin GitHub linkini qo'yamiz

bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --- PDF SHARTNOMA GENERATORI ---
def create_contract(partner_name, commission):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, text="SHUXRAT CINEMA - HAMKORLIK SHARTNOMASI", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, text=f"Hamkor: {partner_name}", ln=1)
    pdf.cell(200, 10, text=f"Komissiya: {commission}%", ln=1)
    pdf.ln(10)
    pdf.multi_cell(0, 10, text="Ushbu shartnoma platforma orqali mijoz topish va xizmat haqi to'lashni tartibga soladi.")

    file_path = f"{partner_name}_shartnoma.pdf"
    pdf.output(file_path)
    return file_path

# --- BOT BUYRUQLARI ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Mini Appni Ochish", web_app=WebAppInfo(url=MINI_APP_URL))]
    ])

    await message.answer(
        "🎬 Shuxrat Cinema botiga xush kelibsiz!\n\n"
        "Portfolioni ko'rish va xizmatlarni bron qilish uchun pastdagi tugmani bosing.",
        reply_markup=markup
    )

@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id in ADMINS:
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➕ Hamkor qo'shish", callback_data="add_partner")],
            [InlineKeyboardButton(text="📊 Hisobotlar", callback_data="reports")]
        ])
        await message.answer("🛠 Admin Boshqaruv Paneli", reply_markup=markup)

@dp.callback_query(F.data == "add_partner")
async def partner_process(callback_query: types.CallbackQuery):
    if callback_query.from_user.id in ADMINS:
        file_path = create_contract("Zebuniso_Toyxonasi", 15)
        document = types.FSInputFile(file_path)
        await bot.send_document(callback_query.from_user.id, document, caption="Yangi hamkor uchun shartnoma tayyor!")
        os.remove(file_path)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot to'xtatildi!")