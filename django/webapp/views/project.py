from .base import BaseView
from webapp.config import PROJECT_MADE_KEY, PROJECT_USED_KEY
from webapp.models import (
    Project,
    ProjectClient,
    ProjectContent,
    ProjectApp,
    ProjectGalerie,
)


class ProjectView(BaseView):
    def setup(self, *args, **kwargs):
        context = super().setup(*args, **kwargs)
        self.view_name = "Project"
        self.template_name = "webapp/project_builder.html"
        self.project_id = kwargs["project_id"]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "project_content_hash": self.build_project_content(
                    self.project_id
                ),
            }
        )
        return context

    def build_project_content(self, project_id):
        """ Build data to manage project content"""
        project_hash = Project.objects.get(pk=project_id)
        container_app_hash = self._build_container_app(project_id)
        return {
            "client_info_list": self._build_container_client(project_id),
            "img_path": project_hash.project_image.path,
            "details": self._build_container_content(project_id),
            "used": container_app_hash[PROJECT_USED_KEY],
            "made": container_app_hash[PROJECT_MADE_KEY],
            "galerie": self._build_container_galerie(project_id),
        }

    def _build_container_client(self, project_id):
        """ Build data to manage project client section"""
        client_info_list = []
        project_client_list = ProjectClient.objects.filter(
            project_id=project_id
        ).order_by("order")
        for project_client_hash in project_client_list:
            client_info_list.append(
                {
                    "name": project_client_hash.name,
                    "value": project_client_hash.value,
                }
            )

        return client_info_list

    def _build_container_content(self, project_id):
        """ Build data to manage project content section"""
        content_list = []
        project_content_list = ProjectContent.objects.filter(
            project_id=project_id
        )
        for project_content_hash in project_content_list:
            content_list.append(project_content_hash.content)

        return "<br/>".join(content_list)

    def _build_container_app(self, project_id):
        """ Build data to manage project app section"""
        result_app_hash = {
            PROJECT_MADE_KEY: [],
            PROJECT_USED_KEY: [],
        }
        app_list = ProjectApp.objects.filter(project_id=project_id)
        for app_hash in app_list:
            type_name = app_hash.app_type_id.app_type_name
            if type_name in result_app_hash:
                result_app_hash[type_name].append(app_hash.name)
        return result_app_hash

    def _build_container_galerie(self, project_id):
        """ Build data to manage project galerie section"""
        result_list = []
        for galerie_hash in ProjectGalerie.objects.filter(
            project_id=project_id
        ):
            result_list.append(
                {"path": galerie_hash.path, "alt": galerie_hash.alt,}
            )
        return result_list
