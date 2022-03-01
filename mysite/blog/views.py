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
            err = createCal(post.email, post.raw_data, post.colour)
            if (err == 0):
                return redirect('complete')
            elif (err == -1):
                return redirect('error')
            else:
                return redirect('error')
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
    first = projects[0]
    return render(request, 'blog/projects.html',{'projects':projects, 'first':first})

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