
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("newpost", views.newpost, name="newpost"),
    path("profile/<str:username>", views.profile, name="profile"),
    
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("like/<int:post_id>", views.like, name="like"),
#    path("/unlike", views.unlike, name="unlike"),
    path("follow/<str:username>", views.follow, name="follow"),
    path("unfollow/<str:username>", views.unfollow, name="unfollow"),
    path("verify/<str:username>", views.verify, name="verify"),
    path("activate/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/", views.activate, name='activate'),

#    path("/editpost", views.editpost, name="editpost"),
#    path("/deletepost", views.deletepost, name="deletepost"),
#    path("/allposts", views.allposts, name="allposts"),

]
