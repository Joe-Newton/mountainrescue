# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Incident(models.Model):
    incidentID = models.AutoField(primary_key = True)
    activity = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    num_people_involved = models.IntegerField()
   

    def __str__(self):
        return str(self.incidentID) + ' - ' +self.activity + ' - ' +self.location 


class PersonInvolved(models.Model):
    name = models.CharField(max_length= 250)
    fatality = models.CharField(max_length=30)
    dob = models.CharField(max_length = 10)
    incidentID = models.ForeignKey(Incident, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.dob


    
