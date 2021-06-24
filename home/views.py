from carrental.settings import BASE_DIR
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

