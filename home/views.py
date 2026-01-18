from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {
        'target_date': "March 20, 2027 00:00:00"
    })