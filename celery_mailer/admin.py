from django.contrib import admin
from .models import StudentDetails, TelegramUser
# Register your models here.

admin.site.register(StudentDetails)
admin.site.register(TelegramUser)