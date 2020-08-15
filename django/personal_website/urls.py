from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import webapp.views

urlpatterns = [
    url(r"^$", webapp.views.HomeView.as_view(), name="home"),
    url(r"^portfolio$", webapp.views.PortfolioView.as_view(), name="portfolio"),
    url(r"^about$", webapp.views.AboutView.as_view(), name="about"),
    url(r"^contact$", webapp.views.ContactView.as_view(), name="contact"),
    url(
        r"^projects/(?P<project_name>[a-z \-]+)/$",
        webapp.views.ProjectView.as_view(),
        name="project",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls)),] + urlpatterns

