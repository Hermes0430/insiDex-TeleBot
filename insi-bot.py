import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext):
    startMsg = "Hello! I am your insiDex-Bot.\n"

    await update.message.reply_text('Hello! I am your insiDex-Bot.')

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text('This command is not avaliable.')

def main():
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Ensure TOKEN is loaded correctly
    if not TOKEN:
        raise ValueError("Telegram bot token is missing. Please check your .env file.")

    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    application.run_polling()
    
if __name__ == '__main__':
    main()