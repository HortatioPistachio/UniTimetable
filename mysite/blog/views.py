from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import postForm
from django.shortcuts import redirect
from .timetableExport import createCal, verifyData
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
    return render(request, 'blog/projects.html')

def error(request):
    return render(request, 'blog/error.html')

