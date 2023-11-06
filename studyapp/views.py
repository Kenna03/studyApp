from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .form import AssignmentForm
from django.http import HttpResponse
from django.template import loader
from .models import Assignment
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studyproject.studyapp.models import Document
from studyproject.studyapp.forms import DocForm


# Create your views here.
@login_required()
def index(request):
    assignments = Assignment.objects.filter(user=request.user)
    form = AssignmentForm()
    return render(request, 'index.html', {'form': form, 'assignments': assignments})


@login_required
@require_POST
def create_assignment(request):
    form = AssignmentForm(request.POST)
    print('preparing to save')
    if form.is_valid():
        assignment = form.save(commit=False)
        assignment.user = request.user
        assignment.save()
        print('saved')
    return redirect('index')


def assignment_s(request):
    myassignments = Assignment.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myassignments': myassignments,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myassignment = Assignment.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myassignment': myassignment,
    }
    return HttpResponse(template.render(context, request))


def details1(request):
    return render(request, "details.html")


def collaboration(request):
    return render(request, "collaboration.html")


def list(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
    if form.is_valid():
        new_doc = Document(doc_file = request.FILES['doc_file'])
        new_doc.save()
        return HttpResponseRedirect(reverse('studyapp.views.list'))
    else:
        form = DocForm()

    docs = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'studyapp/list.html',
        {'documents': docs, 'form': form},
        context_instance=RequestContext(request)
