from django.shortcuts import render

# Create your views here.
 
def index(request):
    # adding context
    return render(request, 'index.html')
