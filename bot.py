import telebot;
import config;

from telebot import types

bot = telebot.TeleBot(config.TOKEN) #получение токена на бота через конфиг файл

# @bot.message_handler(commands=['start']) #start функция
# def start(message):
#     bot.send_message(message.from_user.id, "Приветствую, дорогой гость, информация по кнопкам написана выше, выебри что тебе подходит")

@bot.message_handler(commands=['reserve']) #мэин функция по резерву, далее от нее идут кнопки и ветки
def reserve(message):
    bot.send_message(message.from_user.id, "Для того чтобы забронировать стол, мне нужно немного больше информации.\nНапиши свое имя\nКоличество гостей\nДату и время посещения\nНомер телефона")   
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    # добавляем на нее две кнопки
    button1 = types.InlineKeyboardButton(text="Резерв", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Наш сайт", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)

    # отправляем сообщение пользователю
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=keyboard)

# функция запустится, когда пользователь нажмет на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "button1":
            bot.send_message(call.message.chat.id, "Для того чтобы забронировать стол, мне нужно немного больше информации.\nНапиши свое имя\nКоличество гостей\nДату и время посещения\nНомер телефона")
        if call.data == "button2":
            bot.send_message(call.message.chat.id, "'https://restorani-vdnh.ru/'")

    # if message.text != " ":
    #     bot.send_message(message.from_user.id, "Для того чтоб забронировать стол в нашем заведении нужно заполнить форму бронирования, а также принять наши правила: ' ', продолжая бронь, вы автоматически принимаете их")
    # if message.text != " ":
    #     bot.send_message(message.from_user.id, "На чьё имя бронируем столик?")
    # if message.text != " ":
    #     bot.send_message(message.from_user.id, "Напишите дату и время в формате '01.01 18:15'")
    # if message.text != " ":
    #     bot.send_message(message.from_user.id, "Укажите количество гостей числом")
    #     if message.text != "0" or "1" or "2" or "3":
    #         bot.send_message(message.from_user.id, "Неккоректное количество гостей, введите ещё раз")
    #     else:
    #         bot.send_message(message.from_user.id, "Спасибо за информацию")

@bot.message_handler(commands=['website']) #функция ссылки на сайт
def website_come(message):
    bot.reply_to(message, "'https://restorani-vdnh.ru/'") #ссылка на наш сайт

@bot.message_handler(content_types=["text"]) # Тут ловим все текстовые сообщения от пользователя
def send_from_guest(message): 
    bot.send_message('********', message.text)
    bot.send_message(message.from_user.id, "Спасибо за бронь, менеджер подтвердит её в ближайшее рабочее время заведения (12:00-23:00)")
    bot.send_message(message.from_user.id, "Для повторного резерва нажмите /start или /reserve")
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#         bot.send_message(call.message.chat.id, 'Назад')   
        # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" ",  # remove inline buttons
        # reply_markup=None)
        
# @bot.message_handler(commands=['cancel']) @функция отмены брони
# def cancel_reserve(message):



# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text != " ":
#         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#     elif message.text == "/резерв":
#         bot.send_message(message.from_user.id, "")
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)
