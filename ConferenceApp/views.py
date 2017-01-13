from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from ConferenceApp.models import Session

# Create your views here.
def index(request):
    return render(request, 'ConferenceApp/index.html')


class SessionList(ListView):
    model = Session


class SessionDetail(DetailView):
    model = Session


@login_required
def submit_session(request):
    return render(request, 'ConferenceApp/submit_session.html')