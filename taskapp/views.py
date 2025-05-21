from django.shortcuts import render,redirect
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

class TaskupdateView(APIView):
    permission_classes=[IsAuthenticated]

    def put(self,request,id):
        try:
            task = Task_tb.objects.get(id=id, assigned_to=request.user)
        except Task_tb.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        data=request.data
        if data.get('status') == 'Completed':
            if not data.get('completionreport') or not data.get('worked_hours'):
                return Response({'error': 'Completion report and worked hours are required'}, status=status.HTTP_400_BAD_REQUEST)
            
        serializer=TaskSerializer(task,data=data,partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
class TaskReportView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        try:
            task = Task_tb.objects.get(id=id)
        except Task_tb.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user.role not in ['admin', 'superadmin']:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        if task.status != 'Completed':
            return Response({'error': 'Report only available for completed tasks.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReportSerializer(task)
        return Response(serializer.data)
    
    
    
