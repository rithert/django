from django.http import HttpResponse
from django.template import Template,Context
import datetime


def saludo(request):
    return(HttpResponse("Hola mundo"))

def home(request):
    doc = open("D:/8 Semestre/phyton/PaginaWeb/proyecto1/proyecto1/templates/plantillarither.html")
    plantilla = Template(doc.read())
    doc.close()
    ctx = Context()
    Plant_home = plantilla.render(ctx)
    return(HttpResponse(Plant_home))

def suma(request,a,b):
    today = datetime.date.today()
    suma = a+b
    lista = [1,2,3,4,5]
    doc = open("D:/8 Semestre/phyton/PaginaWeb/proyecto1/proyecto1/templates/plantillasuma.html")
    plantillasuma = Template(doc.read())
    doc.close()
    ct = Context({"valora" :a ,"valorb":b,"suma":suma,"lista":lista,"fecha":today})
    Plant_suma = plantillasuma.render(ct)
    return(HttpResponse(Plant_suma))
    