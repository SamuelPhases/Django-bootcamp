from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    job_list = Job.objects
    context = {
        'jobs': job_list
    }
    return render(request, 'jobs/home.html',context)