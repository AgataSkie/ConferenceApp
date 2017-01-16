from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm

from ConferenceApp.forms import SessionForm
from ConferenceApp.models import Session


def index(request):
    return render(request, 'ConferenceApp/index.html')


class SessionList(ListView):
    model = Session


class SessionDetail(DetailView):
    model = Session


class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm


class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm


class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('conference:sessions_list')
