from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index page that displays frontend or user home page.
def index(request):
    return HttpResponse("Homepage view.")

# Group view that handles particular group page.
def group(request, group_name):
    return HttpResponse("Group view: %s" % group_name)

# User view that handles particular user page.
def user(request, user_name):
    return HttpResponse("User view: %s" % user_name)

# Search view that handles particular search query.
def search(request, search_term):
    return HttpResponse("Search view: %s" % search_term)

# Profile view that handles a users profile.
def profile(request):
    return HttpResponse("Profile view.")

# Settings view that handles a users settings.
def settings(request):
    return HttpResponse("Settings view.")

# Login view that handles the login page.
def login(request):
    return HttpResponse("Login view.")

# Signup view that handles the signup page.
def signup(request):
    return HttpResponse("Signup view.")

# Password reset view that handles the password reset page.
def reset(request):
    return HttpResponse("Reset view.")

