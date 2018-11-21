from django.contrib.auth.models import User
from django.db import models
from enum import Enum
# Create your models here.


class Gender(Enum):
    M = "Male"
    F = "Female"
    OT = "Other"


class Year(Enum):
    Year_1 = '1st Year'
    Year_2 = '2nd Year'
    Year_3 = '3rd Year'
    Year_4 = '4th Year'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    college = models.CharField(max_length=30)
    current_address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Gender], default='')
    current_year_of_study = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Year], default='')
    encarta_id = models.CharField(max_length=30, default='Not Generated')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Event(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=20)
    cost = models.IntegerField(default=0)
    picture = models.ImageField(blank=True)
    prize = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.get_full_name()) + ' --' + str(self.event) + ' ' + str(self.user.profile.encarta_id)