from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from webapp.assets import Assets


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        assets = Assets(self.view_name)
        return {
            "css_list": assets.getCssDependencies,
            "js_list": assets.getJavascriptDependencies,
        }


class HomeView(BaseView):
    template_name = "webapp/home.html"
    view_name = "Home"


class PortfolioView(BaseView):
    template_name = "webapp/portfolio.html"
    view_name = "Portfolio"


class AboutView(BaseView):
    template_name = "webapp/about.html"
    view_name = "About"


class ContactView(BaseView):
    template_name = "webapp/contact.html"
    view_name = "Contact"


class ProjectView(BaseView):
    def setup(self, *args, **kwargs):
        context = super().setup(*args, **kwargs)
        self.template_name = "webapp/projects/{}.html".format(kwargs["project_name"])
        return context

    view_name = "Project"
