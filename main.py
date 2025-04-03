from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text('Hello from Railway!')

app = Application.builder().token("bot-token-here").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
