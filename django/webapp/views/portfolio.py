from .base import BaseView
from webapp.models import Project, ProjectType


class PortfolioView(BaseView):
    template_name = "webapp/portfolio.html"
    view_name = "Portfolio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.build_portfolio_data())
        return context

    def build_portfolio_data(self):
        """ Build data to manage portfolio view"""
        return {
            "project_menu": self.build_portfolio_menu(),
            "project_list": self.build_portfolio_content(),
        }

    def build_portfolio_menu(self):
        """ Build data to manage portfolio menu"""
        menu_list = []
        for project_type_hash in ProjectType.objects.all():
            menu_list.append(
                {"rel": project_type_hash.name, "label": project_type_hash.label}
            )
        return menu_list

    def build_portfolio_content(self):
        """ Build data to manage portfolio content"""
        project_list = []
        for project_hash in Project.objects.all().filter(active=1):
            project_list.append(
                {
                    "id": project_hash.id,
                    "name": project_hash.name,
                    "title": project_hash.title,
                    "sub_title": project_hash.sub_title,
                    "type": project_hash.project_type.name,
                    "img_hash": {
                        "path": project_hash.project_image.vignette_path,
                        "alt": project_hash.project_image.vignette_alt,
                    },
                }
            )
        return project_list
