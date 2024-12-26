from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from src.Oracle.Oracle import Oracle
from src.Oracle.ImprovedOracle import ImprovedOracle
from src.Oracle.AlternateOracle import AlternateOracle
from src.Die import Die

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
    
    template = loader.get_template('oracle.html')
    context = {
       'result': oracle.consult()
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def oracolo_migliorato(request: HttpRequest):
    likelihood = request.POST.get('likelihood')
    improved_oracle = ImprovedOracle(int(likelihood))

    template = loader.get_template('oracle.html')
    context = {
       'result': improved_oracle.consult()
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def oracolo_alternativo(request: HttpRequest):
    likelihood = request.POST.get('likelihood')
    alternate_oracle = AlternateOracle(int(likelihood))

    template = loader.get_template('oracle.html')
    context = {
       'result': alternate_oracle.consult()
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def lancia_dadi(request: HttpRequest):
  number_of_dice = int(request.POST.get('diceNumber'))
  type_of_dice = int(request.POST.get('diceType'))
  dice = Die(number_of_dice, type_of_dice)

  template = loader.get_template('dice.html')
  context = {
      'result': str(dice.throw())
  }
  return HttpResponse(template.render(context, request))