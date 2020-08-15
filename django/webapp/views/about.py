from .base import BaseView


class AboutView(BaseView):
    template_name = "webapp/about.html"
    view_name = "About"
