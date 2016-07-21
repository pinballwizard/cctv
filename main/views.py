from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponse, Http404

# Create your views here.


def test(request):
    data = {
        'video': "Hello"
    }
    return render(request, 'main/test.html', data)