from django.http import HttpResponse
from django.template import loader

from src.Oracle.Oracle import Oracle

def dndapp(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def dice(request):
  template = loader.get_template('dice.html')
  return HttpResponse(template.render())

def oracolo(request):
  template = loader.get_template('oracle.html')
  return HttpResponse(template.render())

def oracolo_base(request):
    
    oracolo = Oracle(0)
    return HttpResponse("Risultato oracolo: " + oracolo.consult())

def oracolo_migliorato(request):
    # Call your Python function here
    return HttpResponse("Oracolo migliorato function triggered")

def oracolo_alternativo(request):
    # Call your Python function here
    return HttpResponse("Oracolo alternativo function triggered")