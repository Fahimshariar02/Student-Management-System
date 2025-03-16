from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name="student_list"),
    path('add_student/', views.add_student, name="add_student"),
    path('update/<int:roll>', views.update, name="update"),
    path('delete/<int:roll>', views.delete, name="delete")
]