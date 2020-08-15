from .base import BaseView


class HomeView(BaseView):
    template_name = "webapp/home.html"
    view_name = "Home"
