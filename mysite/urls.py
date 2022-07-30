from django.urls import path
from django.conf import settings
from . import views


app_name = 'mysite'


urlpatterns = [
    path("",  views.home, name="home_page"),
    path("about/",  views.about, name="about_page"),
    path("services/", views.services, name="services"),
    path("acheivements/", views.acheivements, name="acheivements"),
    path("skills/", views.skills, name="skills")
]

