from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from src.Oracle.Oracle import Oracle
from src.Oracle.ImprovedOracle import ImprovedOracle
from src.Oracle.AlternateOracle import AlternateOracle

def dndapp(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def dice(request):
  template = loader.get_template('dice.html')
  return HttpResponse(template.render())

def oracle(request):
  template = loader.get_template('oracle.html')
  return HttpResponse(template.render())

@csrf_exempt
def oracolo_base(request: HttpRequest):
    likelihood = request.POST.get('likelihood')
    oracle = Oracle(int(likelihood))
    return HttpResponse("The Oracle answered: " + oracle.consult())

@csrf_exempt
def oracolo_migliorato(request: HttpRequest):
    likelihood = request.POST.get('likelihood')
    improved_oracle = ImprovedOracle(int(likelihood))
    return HttpResponse("The Oracle answered: " + improved_oracle.consult())

@csrf_exempt
def oracolo_alternativo(request: HttpRequest):
    likelihood = request.POST.get('likelihood')
    alternate_oracle = AlternateOracle(int(likelihood))
    return HttpResponse("The Oracle answered: " + alternate_oracle.consult())