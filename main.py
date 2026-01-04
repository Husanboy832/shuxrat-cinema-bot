const TelegramBot = require('node-telegram-bot-api');
const express = require('express');

const TOKEN = '7532712344:AAEn-sttm7oaKtqLypaSb7ZINPvPyi5H2P8';
const bot = new TelegramBot(TOKEN, { polling: true });
const app = express();

app.use(express.json());

// Mini App URL
const MINI_APP_URL = 'https://yourdomain.com/miniapp';

// Start command
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    
    const keyboard = {
        reply_markup: {
            inline_keyboard: [
                [
                    {
                        text: '📷 Biznir Sanat Asarvarimiz',
                        web_app:  { url: MINI_APP_URL }
                    }
                ]
            ]
        }
    };

    bot.sendMessage(
        chatId,
        '👋 Salom! Bizning sanat asarvarimizni ko\'rish uchun tugmani bosing: ',
        keyboard
    );
});

// Handle all messages
bot.on('message', (msg) => {
    const chatId = msg. chat.id;
    const text = msg.text;

    if (text !== '/start') {
        bot.sendMessage(chatId, 'Bosh sahifaga qaytish uchun /start ni bosing');
    }
});

// Server
app.listen(3000, () => {
    console.log('Bot running on port 3000');
});
