from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),  # List of students
    path('add/', views.student_add, name='student_add'),  # Form to add a new student
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),  # Delete a student
]
