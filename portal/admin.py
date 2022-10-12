from django.contrib import admin
from .models import Interviewer, Candidate, Interview
# Register your models here.
@admin.register(Interviewer)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('sno','name','email')
    

@admin.register(Candidate)
class CanditateAdmin(admin.ModelAdmin):
    list_display = ('sno','name','email')

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('sno','interviewer','Candidate','date','startTime','endTime','link')


