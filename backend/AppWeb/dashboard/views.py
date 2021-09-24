from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse
from core import models

from . import forms


@login_required
def home(request):
    
    return render(request, 'dashboard/home.html', locals())
