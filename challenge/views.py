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
    teams = session.query(Team)
    employees_teams = session.query(EmployeeTeam)
    employees = session.query(Employee)

    return render(request, 'teams.html', {'teams': teams, 'employees_teams': employees_teams, 'employees': employees})

def recommendation(request):
    recommendations = session.query(Recommendation)

    return render(request, 'recommendations.html', {'recommendations': recommendations})


def add_employee(request):
    name = request.GET['name']
    email = request.GET['email']
    recommended_by = request.GET['recommended']

    check_employee_id(recommended_by)

    new_employee = Employee(full_name=name, email=email, recommended_by=recommended_by)

    session.add(new_employee)
    session.commit()

    response = HttpResponse()

    return response


def add_team(request):
    name = request.GET['name']

    new_team = Team(name=name)

    session.add(new_team)
    session.commit()

    response = HttpResponse()

    return response


def add_recommendation(request):
    name = request.GET['name']
    email = request.GET['email']
    recommended_by = request.GET['recommended']

    check_employee_id(recommended_by)

    new_recommendation = Recommendation(candidate_name=name, candidate_email=email, employee_id=recommended_by)

    session.add(new_recommendation)
    session.commit()

    response = HttpResponse()

    return response


def add_employee_team(request):
    team_id = request.GET['team']
    employee_id = request.GET['employee']

    check_employee_id(employee_id)
    check_team_id(team_id)

    new_employee_team = EmployeeTeam(employee_id=employee_id, team_id=team_id)

    session.add(new_employee_team)
    session.commit()

    response = HttpResponse()

    return response


def update_employee(request):
    return None


def delete_employee(request):
    return None


def check_employee_id(employee_id):
    requested_employee = session.query(Employee).filter(Employee.id == employee_id).first()
    try:
        existing = requested_employee.id
    except:
        raise Exception

    return


def check_team_id(team_id):
    requested_team = session.query(Team).filter(Team.id == team_id).first()
    try:
        existing = requested_team.id
    except:
        raise Exception

    return

# employees = session.query(Employee).order_by(Employee.full_name)
# employee = session.query(Employee).filter(Employee.full_name=="Jose").first()
# employees = session.query(Employee).filter(or_(Employee.full_name=="Jose", Employee.full_name=="Maria")
# employee_count = session.query(Employee).filter(or_(Employee.full_name=="Jose", Employee.full_name=="Maria").count()
