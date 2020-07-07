from django import template
from django.shortcuts import render
import requests

def home(requests):
    return render(requests,'index.html')

def introduction(requests):
    return render(requests,'introduction.html')

def prevention(requests):
    return render(requests,'prevention.html')

def guidelines(requests):
    return render(requests,'guidelines.html')