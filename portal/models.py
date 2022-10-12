from django.db import models
import datetime
# Create your models here.
class Interviewer(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Candidate(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Interview(models.Model):
    sno = models.AutoField(primary_key=True)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE,)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,) 
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    link = models.CharField(max_length=60)
    def __str__(self):
        return self.Candidate.name + ' X ' + self.interviewer.name +' on '+ str(self.date) +" at "+str(self.startTime)


        # admin
        # admn12345