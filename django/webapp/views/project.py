from .base import BaseView
from dictor import dictor
from webapp.models import Project, ProjectClient, ProjectContent


class ProjectView(BaseView):
    def setup(self, *args, **kwargs):
        context = super().setup(*args, **kwargs)
        self.project_id = kwargs["project_id"]
        self.template_name = "webapp/project_builder.html"
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"project_content_hash": self.build_project_content(self.project_id),}
        )
        return context

    view_name = "Project"

    def build_project_content(self, project_id):
        """ Build data to manage project content"""
        project_hash = Project.objects.get(pk=project_id)
        return {
            "client_info_list": self._build_container_client(project_id),
            "project_img_path": project_hash.project_image.path,
            "project_details": self._build_container_content(project_id),
            "project_app": ["Photoshop CS4", "Illustrator CS4"],
            "project_galerie": [
                {
                    "path": "projets/galerie/projet-11/lapero-1.jpg",
                    "alt": "l'apéro.net - 1",
                },
                {
                    "path": "projets/galerie/projet-11/lapero-2.jpg",
                    "alt": "l'apéro.net - 2",
                },
            ],
        }

    def _build_container_client(self, project_id):
        """ Build data to manage project client section"""
        client_info_list = []
        project_client_list = ProjectClient.objects.filter(
            project_id=project_id
        ).order_by("order")
        for project_client_hash in project_client_list:
            client_info_list.append(
                {"name": project_client_hash.name, "value": project_client_hash.value,}
            )

        return client_info_list

    def _build_container_content(self, project_id):
        """ Build data to manage project content section"""
        content_list = []
        project_content_list = ProjectContent.objects.filter(project_id=project_id)
        for project_content_hash in project_content_list:
            content_list.append(project_content_hash.content)

        return "<br/>".join(content_list)
