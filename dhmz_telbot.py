from   os.path import exists as file_exists
from   telegram.ext import *
from   telegram import Update

import commands

periodic_scan_time = 60

def read_all_lines(file_name : str) -> list:
	#procitaj sve jedinstvene linije u fileu
	path = 'data/' + file_name
	if file_exists(path):
		with open(path, 'r') as file:
			data = file.read()
			return list(i for i in filter(lambda x: x != '', data.split('\n')))
	return list()

periodic_chats   = set(int(i) for i in read_all_lines('periodic_chats'))
authorized_chats = set(int(i) for i in read_all_lines('authorized_chats'))
stranice         = read_all_lines('city_codes')

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

	key = ''
	with open('data/bot_token', 'r') as file:
		key = file.read().strip()

	bot = ApplicationBuilder().token(key).build()
	
	bot.add_handler(CommandHandler('help',   commands.help))
	bot.add_handler(CommandHandler('chatid', commands.chatid))
	bot.add_handler(CommandHandler('start',  check(commands.start)))
	bot.add_handler(CommandHandler('stop',   check(commands.stop)))
	bot.add_handler(CommandHandler('list',   check(commands.list)))
	bot.add_handler(CommandHandler('dhmz',    check(commands.dhmz)))#, pass_args=True))

	bot.run_polling()


if __name__ == '__main__':
	main()
