from django.urls import include, path
from . import views
from project_backend.controllers import users_controller
from project_backend.controllers import article_category_controller
from project_backend.controllers import article_controller
from project_backend.controllers import article_like_controller
from project_backend.controllers import alert_controller
from project_backend.controllers import comment_controller
from project_backend.controllers import comment_like_controller
from project_backend.controllers import reply_controller
from project_backend.controllers import reply_like_controller
from project_backend.controllers import missions_controller

urlpatterns = [
    path("", views.index, name="index"),

    #users urls
    path("users/add/", users_controller.add, name="add_user"),
    path("users/login/", users_controller.login, name="login"),
    path("users/get/", users_controller.get, name="get_user"),
    path("users/update/", users_controller.update, name="update_user"),
    path("users/delete/<int:pk>/", users_controller.delete, name="delete_user"),

    #article urls
    path("article/add/", article_controller.add, name="add_article"),
    path("article/get/", article_controller.get, name="get_article"),
    path("article/update/<int:pk>/", article_controller.update, name="update_article"),
    path("article/delete/<int:pk>/", article_controller.delete, name="delete_article"),

    #article category urls
    path("article/add/", article_category_controller.add, name="add_article_category"),
    path("garticle/et/", article_category_controller.get, name="get_article_category"),
    path("article/update/<int:pk>/", article_category_controller.update, name="update_article_category"),
    path("article/delete/<int:pk>/", article_category_controller.delete, name="delete_article_category"),

    #article like urls
    path("article/like/add/", article_like_controller.add, name="add_article_like"),
    path("article/like/get/", article_like_controller.get, name="get_article_like"),
    path("article/like/update/<int:pk>/", article_like_controller.update, name="update_article_like"),
    path("article/like/delete/<int:pk>/", article_like_controller.delete, name="delete_article_like"),

    #comment urls
    path("comment/add/", comment_controller.add, name="add_comment"),
    path("comment/get/", comment_controller.get, name="get_comment"),
    path("comment/update/<int:pk>/", comment_controller.update, name="update_comment"),
    path("comment/delete/<int:pk>/", comment_controller.delete, name="delete_comment"),

    #comment like urls
    path("comment/like/add/", comment_like_controller.add, name="add_comment_like"),
    path("comment/like/get/", comment_like_controller.get, name="get_comment_like"),
    path("comment/like/update/<int:pk>/", comment_like_controller.update, name="update_comment_like"),
    path("comment/like/delete/<int:pk>/", comment_like_controller.delete, name="delete_comment_like"),

    #reply urls
    path("reply/add/", reply_controller.add, name="add_reply"),
    path("reply/get/", reply_controller.get, name="get_reply"),
    path("reply/<int:pk>/", reply_controller.update, name="update_reply"),
    path("reply/<int:pk>/", reply_controller.delete, name="delete_reply"),

    #reply like urls
    path("reply/like/add/", reply_like_controller.add, name="add_reply_like"),
    path("reply/like/get/", reply_like_controller.get, name="get_reply_like"),
    path("reply/like/update/<int:pk>/", reply_like_controller.update, name="update_reply_like"),
    path("reply/like/delete/<int:pk>/", reply_like_controller.delete, name="delete_reply_like"),

    #alert urls
    path("alert/add/", alert_controller.add, name="add_alert"),
    path("alert/get/", alert_controller.get, name="get_alert"),
    path("alert/update/<int:pk>/", alert_controller.update, name="update_alert"),
    path("alert/delete/<int:pk>/", alert_controller.delete, name="delete_alert"),

    #missions urls
    path("missions/add/", missions_controller.add, name="add_mission"),
    path("missions/get/", missions_controller.get, name="get_mission"),
    path("missions/update/<int:pk>/", missions_controller.update, name="update_mission"),
    path("missions/delete/<int:pk>/", missions_controller.delete, name="delete_mission"),
]