from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
from Automan.sqlHelper import SqlHelper
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import F
from django.db import transaction
from django.core.mail import send_mail

from bs4 import BeautifulSoup
import threading
import datetime
import json
import os


def index(request):
    return render(request, 'pages/index.html', locals())


def main(request):
    return render(request, 'pages/main.html', locals())


def config(request):
    return render(request, 'pages/config.html', locals())


def account(request):
    return render(request, 'pages/account.html', locals())


def other(request):
    return render(request, 'pages/other.html', locals())


def publish(request):
    return render(request, 'pages/publish.html', locals())


def upload_file(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        File = request.FILES.get("myFile", None)
        content = request.POST.get('content')
        if File is None:
            return HttpResponse("没有需要上传的文件!")
        else:
            with open("./files/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            sql = SqlHelper()
            import datetime
            time = datetime.datetime.now()
            sql.create('insert into publish(content, media, release_time) VALUES (%s, %s, %s);',[content[0], File.name, time])
            sql.close()
            return HttpResponse("上传成功！请退回上一个地址")