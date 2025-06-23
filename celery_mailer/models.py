from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student_name  = models.CharField(max_length=100)
    student_roll_no = models.IntegerField(unique=True, null=False, blank=False)
    student_email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    
    def __str__(self):
        return f"{self.student_name} - {self.student_roll_no}"
    
    
class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=100, unique = True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username or self.telegram_id
    