from django.contrib import admin
from feedback.models import Feedback

# Register your models here.
class FeedbackResource():
  class Meta:
    model = Feedback

class FeedbackAdmin(admin.ModelAdmin):
  list_display = [
    'id',
    'customer_id',
    'feedback_text',
    'timestamp'
  ]


admin.site.register(Feedback, FeedbackAdmin)
