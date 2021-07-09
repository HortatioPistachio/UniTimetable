from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .forms import postForm
from django.shortcuts import redirect
from .timetableExport import createCal, verifyData
from .models import Project
# Create your views here.

def timetable(request):
    #template = loader.get_template('blog/index.html')
    if request.method == "POST":
        form = postForm(request.POST)
        post = form.save(commit=False)

        #verfiy the data, if not correct send user to error page
        if verifyData(post.raw_data):
            createCal(post.email, post.raw_data)
            return redirect('complete')
        else:
            return redirect('error')
        
    form = postForm()
    return render(request, 'blog/timetable.html', {'form' : form})

def complete(request):
    return render(request, 'blog/complete.html' )

def index(request):
        return render(request, 'blog/index.html')

def about(request):
        return render(request, 'blog/about.html')

def projects(request):
    projects = Project.objects.all()
    first = projects[0]
    return render(request, 'blog/projects.html',{'projects':projects, 'first':first})

def error(request):
    return render(request, 'blog/error.html')

def faq(request):
    return render(request, 'blog/faq.html')

def projectDetail(request, name   ):
    project = get_object_or_404(Project, name=name)
    return render(request, 'blog/projectDetail.html', {'project':project})


def error_404_view(request, exception):
    return render(request, 'blog/error_404.html')