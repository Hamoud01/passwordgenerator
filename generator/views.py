from django.shortcuts import render
from django.http import HttpResponse
import random
def Home (request) :
    return render(request,"generator/home.html")



def password(request):

    characters = list ('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    specialcharacter = list ('!@#$%^&*')

    if request.GET.get('specialcharacter'):
        characters.extend(list ('!@#$%^&*'))

    number = list ('1234567890')
    if request.GET.get('number'):
        characters.extend(list ('1234567890'))

    length = int( request.GET.get('length',12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)



    return render(request,"generator/password.html", {'password': thepassword})


def about (request) :
    return render(request,"generator/about.html", {'about': about})
