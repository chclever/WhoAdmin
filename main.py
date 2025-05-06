import sys, os, telebot
from datetime import datetime

if os.path.exists("logs"):
    pass
else:
    os.mkdir("logs")

def cls():
    os.system("clear")
def get_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def info(message):
    print(f"{get_time()} [INFO]: {message}")
def error(message):
    print(f"[E]: {message} | Error detected at : {get_time()}")

def auto_run():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as err:
            error(err)

def save_file(message):
    if os.path.exists("logs"):
        pass
    else:
        os.mkdir("logs")

    user_info = {
        'username': message.from_user.username,
        'first_name': message.from_user.first_name,
        'last_name': message.from_user.last_name,
        'user_id': message.from_user.id,
        'is_premium': message.from_user.is_premium
    }
        
    info_string = f"""
    > {get_time()}

    • Username: {user_info['username']}
    • Profile Name: {user_info['first_name']} Last Name: {user_info['last_name']}
    • Id: {user_info['user_id']}
    • Premium: {'✓' if user_info['is_premium'] else '✗'}
    """

    with open(f"logs/{get_time()}.log", "+a", encoding="utf-8") as log:
        log.writelines(info_string)

    info(f"[+] Log file has been saved! | {get_time()}.log")
    info(info_string)

if len(sys.argv) != 2:
    error(f"Arguments error. Usage: {sys.argv[0]} <token>")
    exit(5)

token = sys.argv[1]

try:
    bot = telebot.TeleBot(token)

    print("[BOT]: Logging...")

    @bot.message_handler(commands=['start'])
    def handle_start(message):

        info(f"[+] A new User: {message}")
            
        save_file(message)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        user_text = message.text
        
        if not message.text.startswith('/'):
            info(f"{user_text} | ID: {message.from_user.id}")
        else: pass

except Exception as e: 
    error(e)

try:
    bot.polling(none_stop=True)
except Exception as err:
    error(err)
