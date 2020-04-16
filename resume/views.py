from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {

    }
    return render(request, 'homepage.html', context)

def resume(request):
    context = {

    }
    return render(request, 'resume.html', context)
