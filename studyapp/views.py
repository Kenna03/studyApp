from .models import Assignment
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .form import AssignmentForm

# Create your views here.
@login_required()
def index(request):
    assignments = Assignment.objects.filter(user=request.user)
    form = AssignmentForm()
    return render(request, 'index.html', {'assignments': assignments, 'form': form})

@login_required
@require_POST  # Ensure that only POST requests can access this view
def create_assignment(request):
    form = AssignmentForm(request.POST)
    print('preparing to save')
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.user = request.user
        assignment.save()
        print('saved')
    return redirect('index')
