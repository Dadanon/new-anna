import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)


def format_text(text: str) -> str:
    return ' '.join(text.split())


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=format_text(
            f"""
            Привет, {update.effective_user.username},
            я помогу тебе найти любую книгу. Просто
            введи ее название в поле поиска и нажми
            Отправить
            """
        )
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token('6354811387:AAHiw8MNDDXwrnzlPfW8bDofdLOS0BVVm6o').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
