from django.shortcuts import render
from .models import Assignment


# Create your views here.
def index(request):
    assignments = Assignment.objects.all()
    return render(request, 'index.html', {'assignment': assignments})
