import mysql as mysql
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Employee, Team, Recommendation, EmployeeTeam
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///challenge.sqlite", connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()


# Create your views here.
def employee(request):
    employees = session.query(Employee)

    return render(request, 'employees.html', {'employees': employees})


def team(request):
    return None


def recommendation(request):
    recommendations = session.query(Recommendation)

    return render(request, 'recommendations.html', {'recommendations': recommendations})


def add_employee(request):
    name = request.GET['name']
    email = request.GET['email']
    recommended_by = request.GET['recommended']

    check_indicator_employee_by_id(recommended_by)

    new_employee = Employee(full_name=name, email=email, recommended_by=recommended_by)

    session.add(new_employee)
    session.commit()

    response = HttpResponse()

    # raise Exception

    return response


def new_team(request):
    return None


def add_recommendation(request):
    name = request.GET['name']
    email = request.GET['email']
    recommended_by = request.GET['recommended']

    check_indicator_employee_by_id(recommended_by)

    new_recommendation = Recommendation(candidate_name=name, candidate_email=email, employee_id=recommended_by)

    session.add(new_recommendation)
    session.commit()

    response = HttpResponse()

    # raise Exception

    return response


def update_employee(request):
    return None


def delete_employee(request):
    return None


def check_indicator_employee_by_id(id):
    indicator = session.query(Employee).filter(Employee.id == id).first()
    try:
        existing = indicator.id
    except:
        raise Exception

    return

# employees = session.query(Employee).order_by(Employee.full_name)
# employee = session.query(Employee).filter(Employee.full_name=="Jose").first()
# employees = session.query(Employee).filter(or_(Employee.full_name=="Jose", Employee.full_name=="Maria")
# employee_count = session.query(Employee).filter(or_(Employee.full_name=="Jose", Employee.full_name=="Maria").count()
