from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
# Create your views here.
class JobListAPIView(generics.ListAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-posted_date')
    serializer_class = JobSerializer

class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
