from django.shortcuts import render
from .models import Playlist, MovieProxy, TVShowProxy
from django.views.generic import ListView

class PlaylistMixin():
    template_name = 'playlist_list.html'
    title = None
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.title is not None:
            context['title'] = self.title
        return context

    def get_queryset(self):
        return super().get_queryset().published()

class MovieListView(PlaylistMixin, ListView):
    queryset = MovieProxy.objects.all()
    title = "Movies"

class TVShowListView(PlaylistMixin, ListView):
    template_name = 'playlist_list.html'
    queryset = TVShowProxy.objects.all()
    title = "Tv Shows"

class FeaturedPlaylistListView(PlaylistMixin, ListView):
    queryset = Playlist.objects.featured_playlists()
    title = "Featured"