from django.shortcuts import render

# Create your views here.
def home(request):
    List = map(str, range(100))
    return render(request, 'home.html', {'List': List})
