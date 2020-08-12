from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template = loader.get_template("webapp/home.html")
    return HttpResponse(template.render(request=request))


def portfolio(request):
    template = loader.get_template("webapp/portfolio.html")
    return HttpResponse(template.render(request=request))


def about(request):
    template = loader.get_template("webapp/about.html")
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template("webapp/contact.html")
    return HttpResponse(template.render(request=request))


def project(request, project_name):
    template = loader.get_template("webapp/projects/{}.html".format(project_name))
    return HttpResponse(template.render(request=request))
