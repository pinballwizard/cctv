from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import HttpResponse, Http404, FileResponse
from main.models import Device
from django.contrib.auth.decorators import login_required
import subprocess
import av

#ffmpeg -i test.mkv http://localhost:8090/feed1.ffm
cameras = Device.objects.all()

def start_ffserver():
    try:
        subprocess.run(['ffserver', '-d'])
    except:
        print('ffserver dont start')


@login_required
def camlist(request):
    cameras = Device.objects.all()
    data = {
        'devices': cameras
    }
    return render(request, 'main/camlist.html', data)


# @login_required
def test(request):
    if request.is_ajax():
        frame = next(cameras.get_pic())
        response = HttpResponse(content_type='image/jpeg')
        frame.to_image().save(response, 'jpeg')
        return response
    else:
        cameras.connect()
        data = {
            'devices': 'hello'
        }
        return render(request, 'main/test.html', data)


def connect_video_stream(request, pk):
    # print(pk)
    cam = Device.objects.get(pk=pk)
    cam.connect()
    request.session['cam_'+pk] = cam
    # cameras.get(pk=pk).connect()
    # print(cam)
    return HttpResponse('cam')


def image_response(request, pk):
    print(pk)
    if request.is_ajax():
        cam = [cam for cam in cameras if cam.id == int(pk)][0]
        frame = next(cam.get_pic())
        response = HttpResponse(content_type='image/jpeg')
        frame.to_image().save(response, 'jpeg')
        return response
    else:
        cam = [cam for cam in cameras if cam.id == int(pk)][0]
        cam.connect()
        return HttpResponse(cam.connected)