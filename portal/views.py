from django.shortcuts import redirect, render
from portal.models import Interviewer, Candidate, Interview
from django.contrib import messages
import datetime
# Create your views here.
def home(request):
    return render(request,'home.html')

def schedule(request,slug=""):
    print(slug)
    if request.method == 'POST':
        s = True
        interviewerEmail = request.POST.get('interviewerEmail')
        candidateEmail = request.POST.get('candidateEmail')
        link = request.POST.get('link')
        schedule_date = request.POST.get('date')
        today = str(datetime.date.today())
        sd = int(schedule_date.replace("-", ""))
        today = int(today.replace("-", ""))
        if sd < today:
            msg = 'Invalid schedule date'
            messages.error(request,msg)
            s = False
        startTimer = request.POST.get('startTime')
        endTimer = request.POST.get('endTime')
        try:
            interviewer = Interviewer.objects.get(email=interviewerEmail)
        except:
            messages.error(request, "Interviewer not found")
            return redirect('home')
        
        try:
            candidate = Candidate.objects.get(email=candidateEmail)
        except:
            messages.error(request, "Candidate not found")
            return redirect('home')
        i1 = Interview.objects.filter(interviewer = interviewer, date = schedule_date, startTime= startTimer)
        
        i2 = Interview.objects.filter(Candidate = candidate, date = schedule_date, startTime= startTimer)
        if len(i1)==0 and len(i2)==0:
            if slug == "":
                interview = Interview(interviewer=interviewer, Candidate=candidate, date=schedule_date, startTime = startTimer,endTime = endTimer, link=link)
            else:
                interview = Interview.objects.get(sno=slug)
                start_Timer = int(startTimer.replace(":",""))
                interview_endTime = str(interview.endTime)
                interview_endTime = int(interview_endTime.replace(":",""))
                if(start_Timer < interview_endTime):
                    msg = "Interview cannot be scheduled"
                    messages.success(request, msg)
                    s = False
                else:
                    interview.interviewer = interviewer
                    interview.candidate = candidate
                    interview.date = schedule_date
                    interview.startTime = startTimer
                    interview.endTime = endTimer
                    interview.link = link
            if s == True:
                interview.save()
                msg= "Interview scheduled for "+candidate.name+" by "+interviewer.name+" \n on "+schedule_date + " at time"+ startTimer
                messages.success(request, msg)

        if(len(i1) != 0):
            msg = "Interview cannot be scheduled beacuse "+interviewer.name+ ' has an interview scheduled on '+ schedule_date+ ' at time'+ startTimer
            messages.success(request, msg)
        if(len(i2) != 0):
            msg = "Interview cannot be scheduled beacuse "+candidate.name+ ' has an interview scheduled on '+ schedule_date+ " at time"+ startTimer
            messages.success(request, msg)
    return redirect('home')
    
def upcoming(request):
    interview = Interview.objects.all()
    context={"interviews":interview}
    return render(request, 'upcoming.html', context)

def edit(request,slug):
    inter = Interview.objects.get(sno=slug)
    context = {'interview':inter}
    return render(request, 'edit.html',context)

def confirmEdit(request,slug):
    slug = str(slug)
    schedule(request, slug)
    return redirect("home")


def delete(request, slug):
    inter = Interview.objects.get(sno=slug)
    name = Interview.objects.get(sno=slug).Candidate.name
    inter.delete()
    msg = "interview id "+slug+" " + name+" deleted successfully."
    messages.success(request, msg)
    return redirect("upcoming")

def open(request, slug, slug2):
    inter = Interview.objects.get(sno = slug, link = slug2)
    if slug2 == inter.Candidate.email:

        contents = {"interview":inter}
        return render(request, "open.html",contents)
    else:
        messages.success(request, "Not authorized to open this link.")
        return redirect("upcoming")