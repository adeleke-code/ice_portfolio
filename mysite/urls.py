from django.urls import path
from . import views


app_name = 'mysite'

page = ('adeleke.herokuapp.com/')
urlpatterns = [
    path(f"page",  views.home, name="home"),
    path("about/",  views.about, name="about_page"),
    path("services/", views.services, name="services"),
    path("acheivements/", views.acheivements, name="acheivements"),
    path("skills/", views.skills, name="skills"),
]
