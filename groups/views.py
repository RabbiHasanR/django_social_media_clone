from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember

# Create your views here.

class CreatGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(generic.DetailView):
    model=Group

class ListGroups(generic.ListView):
    model=Group
