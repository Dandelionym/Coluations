from django.db.models import Count
from django.shortcuts import render, HttpResponse, redirect
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