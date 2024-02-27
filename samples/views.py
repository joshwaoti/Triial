from django.shortcuts import render
from samples.serializers import CustomerComplaintsSerializer,ScheduledDirectorsSerializer,MobileInformationSerializer
from .models import CustomerComplaints,ScheduledDirectors,MobileInformation
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CustomerComplaintsApiView(generics.GenericAPIView):
    queryset = CustomerComplaints.objects.all()
    serializer_class = CustomerComplaintsSerializer


    def get(self, request):
        queryset = self.get_queryset()
        serializer = CustomerComplaintsSerializer(queryset, many=True)
        return Response(serializer.data)



    
class ScheduledDirectorsApiView(generics.GenericAPIView):
    queryset = ScheduledDirectors.objects.all()
    serializer_class = ScheduledDirectorsSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ScheduledDirectorsSerializer(queryset, many=True)
        return Response( serializer.data)
    
      
    def post(self, request, format=None):
        serializer = ScheduledDirectorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


   
class MobileInformationApiView(generics.GenericAPIView):
    queryset = MobileInformation.objects.all()
    serializer_class = MobileInformationSerializer


    def get(self, request):
        queryset = self.get_queryset()
        serializer = MobileInformationSerializer(queryset, many=True)
        return Response( serializer.data)
    
    
    def post(self, request, format=None):
        serializer = MobileInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)