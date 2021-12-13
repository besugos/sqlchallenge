from django.contrib import admin
from django.urls import path

from . import views

# from screens.views import ScreenView
app_name = 'challenge'

urlpatterns = [
    path('', views.employee_list, name="employee_list"),
    path('teams', views.teams_list, name="teams_list"),
    path('recommendations', views.recommendations_list, name="recommendations_list"),
    path('newemployee', views.new_employee, name="create_employee"),
    path('newteam', views.new_team, name="create_team"),
    path('newindication', views.new_indication, name="create_indication"),
    path('updateemployee/<int:id>/', views.update_employee, name="update_employee"),
    path('deleteemployee/<int:id>/', views.delete_employee, name="delete_employee"),
]
