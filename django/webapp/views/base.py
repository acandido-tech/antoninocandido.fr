from django.views.generic import TemplateView
from webapp.assets import Assets


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assets = Assets(self.view_name)
        context.update(
            {
                "css_list": assets.getCssDependencies,
                "js_list": assets.getJavascriptDependencies,
            }
        )
        return context
