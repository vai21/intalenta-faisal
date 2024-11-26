from .models import Feedback
from django.db import transaction
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['customer_id', 'feedback_text', 'timestamp']

