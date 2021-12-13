from django.db import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Create your models here.
# class Employee(models.Model):
#     id = models.IntegerField()
#     full_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     recommended = models.BooleanField()
#     recommended_by = models.IntegerField()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    email = Column(String(255))
    recommended_by = Column(Integer)


# class Team(models.Model):
#     id = models.IntegerField()
#     name = models.CharField(max_length=255)


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))


# class Recommendation(models.Model):
#     id = models.IntegerField()
#     employee_id = models.IntegerField()
#     candidate_name = models.CharField(max_length=255)
#     candidate_email = models.CharField(max_length=255)

class Recommendation(Base):
    __tablename__ = 'recommendation'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    candidate_name = Column(String(255))
    candidate_email = Column(String(255))


# class EmployeeTeam(models.Model):
#     id = models.IntegerField()
#     employee_id = models.IntegerField()
#     team_id = models.IntegerField()

class EmployeeTeam(Base):
    __tablename__ = 'employee_team'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    team_id = Column(Integer)
