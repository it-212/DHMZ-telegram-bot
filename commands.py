from   telegram.ext import *
import telegram
from   telegram import Update
import dhmz_telbot
import screenshot

file = open('data/help', 'r')
help_text = "".join(i for i in file.readlines())
file.close()

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
   
async def chatid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_chat.id)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("start")	

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="stop")

async def list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="list")
    
async def dhmz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    screenshot.get()
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('screenshot.png', 'rb'))
    
   
