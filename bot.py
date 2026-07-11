from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv"8355095390:AAEyGFlJJM4GGCDiK6O2bpwK7i3QozhMG3Q"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        movie = context.args[0]
        await update.message.reply_text(f"You requested: {movie}")
    else:
        await update.message.reply_text("Welcome! Please open the bot using your movie link.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

import asyncio

async def main():
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
