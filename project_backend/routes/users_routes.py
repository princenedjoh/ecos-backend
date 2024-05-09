from django.urls import path

from project_backend.controllers import users

urlpatterns = [
    path("add/", users.add, name="add_users"),
    path("get/", users.get, name="get_users"),
]