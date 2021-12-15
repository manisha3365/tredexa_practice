from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("User app")

def add_(request):
    return render(request,'users/index.html')