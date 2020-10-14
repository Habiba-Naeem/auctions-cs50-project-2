from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add/listing", views.listing, name="addlisting"),
    path("<int:id>", views.view_list, name="list"),
    path("add/watchlist/<int:id>", views.addwatchlist, name="addwatchlist"),
    path("remove/watchlist/<int:id>", views.remove, name="remove"),
    path("bid/<int:id>", views.bid, name="bid")
]
