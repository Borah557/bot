from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text('Hello from Railway!')

app = Application.builder().token("7972508793:AAGliWtKAbzXCEM4cvZYgB4JRgzG4HSpxeY").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
