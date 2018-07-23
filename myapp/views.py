from django.shortcuts import render
from django.http import HttpResponse
# from  gpiozero import LED

import json

bookmarks = [{'site': 'naver', 'url': 'http://www.naver.com'},
             {'site': 'daum', 'url': 'http://www.daum.net'},
             {'site': 'google', 'url': 'http://www.google.com'},
             ]

def get_bookmarks(request):
    context = {'bookmarks': bookmarks}
    site = request.GET.get('site')
    url = request.GET.get('url')

    global bookmarks

    if site:
        bookmark = {'site': site, 'url': url}
        bookmarks.append(bookmark)

    return HttpResponse(json.dumps(context), content_type='application/json')

def set_led(request):
    led = request.GET.get('led')
    # hw_led = LED(17)

    # if led == 'on':
    #     hw_led.on()
    # elif led == 'off':
    #     hw_led.off()

    context = {'led':led}
    return render(request, 'led.html', context)

def bookmark_list(request):
    site = request.GET.get('site')
    url = request.GET.get('url')

    global bookmarks

    if site:
        bookmark = {'site': site, 'url': url}
        bookmarks.append(bookmark)

    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarkList.html', context)

def mem_ber_list(request):
    members = ['Song', 'Lee', 'Kim']
    context = {'members':members}
    return render(request, 'memberList.html', context)

def home(request):
    title = request.GET.get('title')
    aaa_param = request.GET.get('aaa')
    content = {'title': title,
               'aaa':aaa_param,
               }
    return render(request, 'home.html', content)

# Create your views here.
