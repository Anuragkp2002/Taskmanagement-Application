from django.urls import path, include
from .views import*




urlpatterns=[
    path('task/',GettaskApiView.as_view(),name='GettaskApiView'),
    path('task/<int:id>',TaskupdateView.as_view(),name='TaskupdateView'),
    path('tasks/<int:id>/report/', TaskReportView.as_view(), name='TaskReportView'),
    
    
    
    
    
    
]