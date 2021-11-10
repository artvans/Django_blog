from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def post1(request):
    return render(request, 'core/post1.html')

def post2(request):
    return render(request, 'core/post2.html')

def post3(request):
    return render(request, 'core/post3.html')