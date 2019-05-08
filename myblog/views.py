from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
import django.contrib.auth as auth
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
import dateutil.parser as dateparser
import json
from django.utils.timezone import activate
from django.conf import settings
# Create your views here.
def index(request):
	return render(request, 'myblog/index.html', {})

