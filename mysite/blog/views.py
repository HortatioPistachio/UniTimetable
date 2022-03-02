'''
to get the ical to work it needs to be a url to a file, not a webpage of it, need to work out a way to autodownload the ical
with the given txt
'''

from calendar import calendar
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .forms import postForm
from django.shortcuts import redirect
from .timetableExport import createCalGoogle, createCalICal, verifyData
from .models import Project, iCal_calendar
# Create your views here.

def timetable(request):
    #template = loader.get_template('blog/index.html')
    if request.method == "POST":
        form = postForm(request.POST)
        post = form.save(commit=False)

        #verfiy the data, if not correct send user to error page
        if verifyData(post.raw_data):
            if (post.cal_type == 'Google'):
                createCalGoogle(post.email, post.raw_data)
                return redirect('complete')

            if (post.cal_type == 'iCal'):
                code = createCalICal(post.email, post.raw_data)
                return redirect('iCal_complete', code) 

            
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
    projects = Project.objects.order_by('-year')
    p = 0
    first = []
    projectList = []
    while p < projects.count():
        first.append(projects[p])
        p += 1
        for p2 in range(p, p+4):
            if p2 >= projects.count():
                break

            projectList.append(projects[p2])
        p += 5
            
    return render(request, 'blog/projects.html',{'projectList':projectList, 'first':first})

def error(request):
    return render(request, 'blog/error.html')

def faq(request):
    return render(request, 'blog/faq.html')

def projectDetail(request, name):
    project = get_object_or_404(Project, name=name)
    pictures = [project.img1]
    try:
       project.img2.size
       pictures.append(project.img2)
    except:
        pass

    try:
       project.img3.size
       pictures.append( project.img3)
    except:
        pass

    numPics = range(len(pictures))
    return render(request, 'blog/projectDetail.html', {'project':project, 'pictures':pictures, 'numPics':numPics})


def error_404_view(request, exception):
    return render(request, 'blog/error_404.html')

def iCalLink(request, name):
    calendar = get_object_or_404(iCal_calendar, name=name)
    cal_data = calendar.cal
    return render(request, 'blog/iCal_template.html', {'cal':cal_data}, content_type="text/calendar")

def iCal_complete(request, code):
    return render(request,'blog/iCal_complete_template.html', {'cal_code':code} )
