from ai21 import AI21Client
from ai21.models.chat import UserMessage
from statistics import mode
from celery import shared_task
from .serializers import FeedbackSerializer

# One way of passing your key to the client.
client = AI21Client(api_key="your api key")

# Another way to set your key is by setting the AI21_API_KEY
# environment variable to your key value. The default value
# of api_key in the constructor is os.environ["AI21_API_KEY"]. So:
# import os
# os.environ["AI21_API_KEY"] =  <YOUR_API_KEY>
# client = AI21Client();

def single_message_instruct(content):
    messages = [
        UserMessage(
            content=f"Give an average sentiment for this array of feedback message (Negative, Neutral, Positive) {content}. Please respond with one word only (Negavite or Neutral or Positive)"
        )
    ]

    response = client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        top_p=1.0 # Setting to 1 encourages different responses each call.
    )
    print(response.choices[0].message)
    return f"The average feedback is: {response.choices[0].message.content}"


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
    max_freq = "Word with maximum frequency : " + str(res)
    print(max_freq)
    return max_freq
  # all words array
  all_words = []
  # all feedbacks words
  all_feedbacks = []
  for feedback in data:
    # print(feedback['feedback_text'])
    words = feedback['feedback_text'].split(' ')
    all_feedbacks.append(feedback['feedback_text'])
    for word in words:
      all_words.append(word)
  # get top keyword
  top_keyword = get_max_word(all_words)
  average_sentiment = single_message_instruct(all_feedbacks)
  # serialize data and save to db
  serializer = FeedbackSerializer(data=data, many=True)
  if serializer.is_valid():
    instances = serializer.save()
    if instances:
      print(f"Saved {len(instances)} feedback entries")
      return {"status": "success", "message": f"Saved {len(instances)} {top_keyword} | {average_sentiment}"}
    else:
      print("Serializer.save() returned None")
      return {"status": "error", "message": "No instances were saved"}
  else:
      return {"status": "error", "errors": serializer.errors}
