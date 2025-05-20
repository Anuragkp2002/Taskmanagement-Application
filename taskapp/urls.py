from django.urls import path, include
from .views import*




urlpatterns=[
    path('GettaskApiView/',GettaskApiView.as_view(),name='GettaskApiView')
]