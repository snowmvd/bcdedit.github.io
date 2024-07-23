import telebot.types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

webapp = telebot.types.WebAppInfo("https://google.com")

markup_menu = InlineKeyboardMarkup()
markup_menu.row_width = 1
markup_menu.add(
    InlineKeyboardButton(text="Перейти в приложение", web_app=webapp),
    InlineKeyboardButton("Помощь", callback_data="help")
)

