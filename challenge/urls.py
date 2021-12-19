from django.contrib import admin
from django.urls import path

from . import views

# from screens.views import ScreenView
app_name = 'challenge'

urlpatterns = [
    path('', views.employee, name="employee_list"),
    path('teams', views.team, name="teams_list"),
    path('recommendations', views.recommendation, name="recommendations_list"),
    path('createemployee', views.add_employee, name="create_employee"),
    path('createrecommendation', views.add_recommendation, name="create_recommendation"),
    path('newteam', views.new_team, name="create_team"),
    path('update_employee/<int:id>/', views.update_employee, name="update_employee"),
    path('deleteemployee/<int:id>/', views.delete_employee, name="delete_employee"),
]
