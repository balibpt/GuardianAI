from telegram.ext import ApplicationBuilder, MessageHandler, filters
from backend.config import TELEGRAM_TOKEN
from bot.handlers import handle_text

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.run_polling()
