from .base import BaseView
from dictor import dictor
from webapp.config import PROJECTS_CONFIG


class ProjectView(BaseView):
    def setup(self, *args, **kwargs):
        context = super().setup(*args, **kwargs)
        self.project_name = kwargs["project_name"]
        self.template_name = "webapp/project_builder.html"
        return context

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(
            {"project_content_hash": dictor(PROJECTS_CONFIG, self.project_name),}
        )
        return context

    view_name = "Project"
