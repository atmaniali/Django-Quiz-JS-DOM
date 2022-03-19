from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('getQuestion/<str:title>/', views.getQuestion, name='test')
]
