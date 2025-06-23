# Kanhaiya-Lal-Bohra-Internship

intership_assingemet_api_dj_rest/
├── Main_project_intern/
│   └── settings.py
├── celery_mailer/
│   ├── models.py
│   ├── views.py
│   ├── bot.py
├── manage.py
├── requirements.txt
└── .env

## Start main project
python manage.py runserver
go to http://127.0.0.1:8000/student/api/

## POST /api/register/
{
  "username": "john",
  "password": "123456",
  "email": "john@example.com"
}

## admin panal
python manage.py createsuperuser
add username and password
http://127.0.0.1:8000/admin/
 
## Create a .env file in the root:
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

## email.env
EMAIL_HOST_USER=Place_gmail
EMAIL_HOST_PASSWORD=place_pass_without_space

##  Start Celery worker (in another terminal)
celery -A Main_project_intern worker --loglevel=info --pool=solo

##  Run Telegram bot (in another terminal)
cd .\Main_project_intern\celery_mailer python celery_mailer/bot.py

## Telegram Bot Flow
User sends /start to your bot.
Telegram username, user_id, and first_name are stored in Django DB.

