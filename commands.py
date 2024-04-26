from   telegram.ext import *
import telegram
from   telegram import Update
import screenshot

import file_utils

file = open('data/help', 'r')
help_text = "".join(i for i in file.readlines())
file.close()

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
    screenshot.get()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('screenshot.png', 'rb'))
    
   
