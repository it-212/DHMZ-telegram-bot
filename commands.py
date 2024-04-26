from   telegram.ext import *
import telegram
from   telegram import Update
import json

import file_utils
import screenshot

file = open('data/help', 'r')
help_text = "".join(i for i in file.readlines())
file.close()

def map_city_code(city_name : str):
    json_file = open("./data/city_codes", "r")
    city_codes = json.load(json_file)
    json_file.close()
    if(city_name not in city_codes):
        return "error"
    return city_codes[city_name]

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
   
async def chatid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_utils.add_line("periodic_chats", str(update.effective_chat.id))
    await update.message.reply_text("Dodano na listu za periodičko slanje prognoze")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_utils.remove_line("periodic_chats", str(update.effective_chat.id))
    await update.message.reply_text("Maknuto s liste za periodičko slanje prognoze")

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="list")
    
async def dhmz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    poruka = update.message.text[5:].strip()
    city_name = poruka if poruka != "" else "Zagreb Gric" 
    try:
        city_code = map_city_code(city_name.strip())
        if(city_code=="error"):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Pogresan kod grada.")
            return
        screenshot.get(city_code)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('screenshot.png', 'rb'))
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Neuspjelo dohvaćanje prognoze.")
        
   
