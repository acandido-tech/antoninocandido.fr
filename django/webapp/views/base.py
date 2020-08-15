from django.views.generic import TemplateView
from webapp.assets import Assets


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        assets = Assets(self.view_name)
        return {
            "css_list": assets.getCssDependencies,
            "js_list": assets.getJavascriptDependencies,
        }
