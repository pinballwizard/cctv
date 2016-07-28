from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponse, Http404
from main.models import Device
import subprocess

#ffmpeg -i test.mkv http://localhost:8090/feed1.ffm


def start_ffserver():
    try:
        subprocess.run(['ffserver', '-d'])
    except:
        print('ffserver dont start')

# def videostream_connect():


def camlist(request):
    data = {
        'devices': Device.objects.all()
    }
    return render(request, 'main/camlist.html', data)


def test(request):
    data = {
        'devices': Device.objects.all()
    }
    return render(request, 'main/test.html', data)
