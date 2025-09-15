from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("start-domain/<int:id>/", views.start_domain, name="start_domain"),   # NEW
    path("domain/<int:id>/", views.domain_view, name="domain_view"),
    path("result/", views.results_view, name="result"),
]
