from django.shortcuts import render
from taskapp.urls import*
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from taskapp.models import*
from taskapp.serializers import*
from rest_framework.response import Response
from rest_framework import status

# Create your views here.




class GettaskApiView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        try:
            task_obj=Task_tb.objects.filter(assigned_to=request.user)
            serializer=TaskSerializer(task_obj,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
