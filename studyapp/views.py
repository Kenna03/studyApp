from django.shortcuts import render
from .models import Assignment
from django.shortcuts import render, redirect
from .forms import AssignmentForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    assignments = Assignment.objects.all()
    return render(request, 'index.html', {'assignment': assignments})
