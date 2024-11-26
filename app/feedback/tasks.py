from celery import shared_task
from rest_framework import serializers
from .models import Feedback
from .serializers import FeedbackSerializer

@shared_task
def process_bulk_insert(data):

  import time
  time.sleep(30)
  serializer = FeedbackSerializer(data=data, many=True)
  if serializer.is_valid():
    instances = serializer.save()
    if instances:
      print(f"Saved {len(instances)} feedback entries")
      return {"status": "success", "message": f"Saved {len(instances)} feedback entries"}
    else:
      print("Serializer.save() returned None")
      return {"status": "error", "message": "No instances were saved"}
  else:
      return {"status": "error", "errors": serializer.errors}
  # return data
