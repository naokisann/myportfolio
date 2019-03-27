from django.shortcuts import render


#Access to the model
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects

    return render(request, 'jobs/home.html', {'jobs':jobs})
