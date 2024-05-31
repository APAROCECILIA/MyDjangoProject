from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    corn_dict = {'insert_me': "I am from views.py in FirstApp!"}
    return render(request, 'FirstApp/corns.html', context=corn_dict)

def pageHola(request):
    hola_dict = {'hola_page': " views.py connected to cecilia.html in FirstApp!"}
    return render(request, 'FirstApp/cecilia.html', context=hola_dict)
