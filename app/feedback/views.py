# from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer
from .tasks import process_bulk_insert
from celery.result import AsyncResult
from customerfeedbackanalysis.celery import app

# Create your views here.
class FeedbackView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by('-timestamp')
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs): 
        task = process_bulk_insert.delay(request.data)  # asynchronously insert bulk feedback data to the database
        try:  
          return Response({ 'task_id': task.id, 'state': task.state, 'result': task.result }, status=status.HTTP_201_CREATED)  
        except Exception as e:  
          return Response(e, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET'])
def get_task_result(request):
  task_id = request.GET.get('task_id', None)
  result = AsyncResult(task_id, app=app)
  return Response({
      'task_id': task_id,
      'status': result.status,
      'result': result.result,  # Contains the task's output or exception
  }, status=status.HTTP_200_OK)
