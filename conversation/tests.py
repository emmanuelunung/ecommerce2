from django.shortcuts import render
from django.test import TestCase

# Create your tests here.
def home(request):
    context = {}
    return render(request, "conversation/home.html", context)

