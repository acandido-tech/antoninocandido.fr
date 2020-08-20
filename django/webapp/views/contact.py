from .base import BaseView


class ContactView(BaseView):
    template_name = "webapp/contact.html"
    view_name = "Contact"
