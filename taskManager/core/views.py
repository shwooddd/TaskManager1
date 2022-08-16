from django.http import HttpResponse
from random import randint

def index(request):
    a = randint(0, 1000)
    return HttpResponse(f'u was is pidoras {str(a)} raz')