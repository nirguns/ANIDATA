from django.urls import path
from .views import ListToDo,DetaliToDo

urlpatterns = [
    path('', ListToDo.as_view()),
    path('<int:pk>/',DetaliToDo.as_view()),
]
