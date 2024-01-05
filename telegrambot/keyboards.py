from telebot import types

def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('озвучить')
    button2 = types.KeyboardButton('профиль')
    button3 = types.KeyboardButton("попытки")
    
    keyboard.row(button1, button2)
    keyboard.row(button3)
    
    return keyboard

def get_cancel_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("отмена")
    keyboard.row(button1)
    
    return keyboard

def get_buy_attempts():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    button1 = types.KeyboardButton("купить попытки")
    button2 = types.KeyboardButton("отмена")
    
    keyboard.row(button1, button2)
    
    return keyboard
