from django.urls import path
from . import views

urlpatterns = [
    path("home",  views.home, name="home"),
    path("about/",  views.about, name="about_page"),
    path("services/", views.services, name="services"),
    path("acheivements/", views.acheivements, name="acheivements"),
    path("skills/", views.skills, name="skills"),
]
