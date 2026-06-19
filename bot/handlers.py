async def handle_text(update, context):
    text = update.message.text
    await update.message.reply_text(f"Echo: {text}")