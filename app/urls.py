from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),  # Added 'name' attribute
    path("home/", views.home, name="home"),  # Added 'name' attribute
    path("regi/", views.regi, name="regi"),
    path("show/", views.person_list, name="person_list"),
    path(
        "logout/", views.logout_view, name="logout"
    ),  # Changed 'logout_view/' to 'logout/' for better readability
]
