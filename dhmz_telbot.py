from   telegram.ext import *
from   telegram import Update

import commands
import file_utils

periodic_scan_time = 60

periodic_chats   = file_utils.get_content('periodic_chats')
authorized_chats = file_utils.get_content('authorized_chats')
stranice         = file_utils.read_all_lines('city_codes')

def check(commandFunc):
	#provjeri je li chat ovlasten za komunikaciju s botom
	async def check_chatid(update : Update, context : CallbackContext) -> None:
		if update.message.chat_id not in authorized_chats:			
			await update.message.reply_text("chatid error")
			await update.message.reply_text(update.message.chat_id)
			for chat in authorized_chats:
				await update.message.reply_text(chat)				
			return
		await commandFunc(update, context)
	return check_chatid

def main():
	for line in authorized_chats:
		print(line)

	key = ''
	with open('data/bot_token', 'r') as file:
		key = file.read().strip()

	bot = ApplicationBuilder().token(key).build()
	
	bot.add_handler(CommandHandler('help',   commands.help))
	bot.add_handler(CommandHandler('chatid', commands.chatid))
	bot.add_handler(CommandHandler('start',  check(commands.start)))
	bot.add_handler(CommandHandler('stop',   check(commands.stop)))
	bot.add_handler(CommandHandler('list',   check(commands.list)))
	bot.add_handler(CommandHandler('dhmz',    check(commands.dhmz)))

	bot.run_polling()


if __name__ == '__main__':
	main()
