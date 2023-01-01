from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def product3d(request):
  template = loader.get_template('product3d.html')
  return HttpResponse(template.render())