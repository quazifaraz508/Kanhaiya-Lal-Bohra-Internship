import os
import sys
import django
from telegram.ext import Updater, CommandHandler
from decouple import config

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Main_project_intern.settings")
django.setup()

# Import TelegramUser model
from celery_mailer.models import TelegramUser

TELEGRAM_TOKEN = "Your_Token" #I remove my bots token you can put yours

def start(update, context):
    user = update.message.from_user
    TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name
        }
    )
    update.message.reply_text("Welcome! You have been registered 🎉")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
