from django.http import HttpResponse
from django.template import loader

def dndapp(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def dice(request):
  template = loader.get_template('dice.html')
  return HttpResponse(template.render())

def oracle(request):
  template = loader.get_template('oracle.html')
  return HttpResponse(template.render())