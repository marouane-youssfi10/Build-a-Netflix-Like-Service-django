"""djangoflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from playlists.views import MovieListView, TVShowListView, FeaturedPlaylistListView


urlpatterns = [
    # re_path(r'my-detail/(?P<id>\d+)/$', FeaturedPlaylistListView.as_view()),

    path('admin/', admin.site.urls),

    path('', FeaturedPlaylistListView.as_view()),

    path('movies/<slug:slug>/', MovieListView.as_view()),
    path('movies/', MovieListView.as_view()),

    path('media/<int:id>/', FeaturedPlaylistListView.as_view()),

    path('shows/<slug:showSlug>/seasons/<slug:seasonSlug>/', TVShowListView.as_view()),
    path('shows/<slug:slug>/seasons/', TVShowListView.as_view()),
    path('shows/<slug:slug>/', TVShowListView.as_view()),
    path('shows/', TVShowListView.as_view()),
]