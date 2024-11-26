from django.db import models

from datetime import datetime

# Create your models here.
class Feedback(models.Model):
  def __int__(self):
    return self.id
  
  id = models.AutoField(primary_key=True)
  customer_id = models.IntegerField(verbose_name='Customer ID')
  feedback_text = models.TextField(verbose_name='Feedback Text')
  timestamp = models.DateTimeField(default=datetime.now)
  
