import telebot 
from plus import tokens
from plus import inl

# Инициализация бота
bot = telebot.TeleBot(tokens.main)

# /start
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(
        chat_id, "*Органический трафик обнадёживает*\n \nВысокий уровень вовлечения представителей целевой аудитории является четким доказательством простого факта: начало повседневной работы по формированию позиции, а также свежий взгляд на привычные вещи — безусловно открывает новые горизонты для новых принципов формирования материально-технической и кадровой базы.",
        reply_markup = inl.markup_menu, parse_mode="Markdown"
    )
    
# Обработка инлайн
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Помощь #
    if call.data == "help":
        print("Пользователь запросил помощь")

if __name__ == "__main__":
    print(f"Бот запущен: @{bot.get_me().username}")
    bot.infinity_polling()
