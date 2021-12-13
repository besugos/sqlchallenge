import mysql as mysql
from django.shortcuts import render
from .models import Employee, Team, Recommendation, EmployeeTeam
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/simbiose_challenge")
Session = sessionmaker(bind=engine)
session = Session()


# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def teams_list(request):
    return None


def recommendations_list(request):
    return None


def new_employee(request):
    return None


def new_team(request):
    return None


def new_indication(request):
    return None


def update_employee(request):
    return None


def delete_employee(request):
    return None