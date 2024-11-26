from statistics import mode
from celery import shared_task
from rest_framework import serializers
from .models import Feedback
from .serializers import FeedbackSerializer

@shared_task
def process_bulk_insert(data):

  def get_max_word(test_list):
    # printing original list
    print("The original list is : " + str(test_list))
    
    # getting all words
    temp = [wrd for sub in test_list for wrd in sub.split()]
    
    # getting frequency
    res = mode(temp)
    
    # printing result
    print("Word with maximum frequency : " + str(res))
    max_freq = "Word with maximum frequency : " + str(res)
    return max_freq

  all_words = []
  for feedback in data:
    # print(feedback['feedback_text'])
    words = feedback['feedback_text'].split(' ')
    for word in words:
      all_words.append(word)

  top_keyword = get_max_word(all_words)

  serializer = FeedbackSerializer(data=data, many=True)
  if serializer.is_valid():
    instances = serializer.save()
    if instances:
      print(f"Saved {len(instances)} feedback entries")
      return {"status": "success", "message": f"Saved {len(instances)} {top_keyword}"}
    else:
      print("Serializer.save() returned None")
      return {"status": "error", "message": "No instances were saved"}
  else:
      return {"status": "error", "errors": serializer.errors}
