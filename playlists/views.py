from django.shortcuts import render
from .models import MovieProxy, TVShowProxy
from django.views.generic import ListView

class TitleMixin():
    title = None
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['title'] = self.title
        return context

class MovieListView(TitleMixin, ListView):
    template_name = 'playlist_list.html'
    queryset = MovieProxy.objects.all()
    title = "Movies"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        context['title'] = self.title
        return context

class TVShowListView(TitleMixin, ListView):
    template_name = 'playlist_list.html'
    queryset = TVShowProxy.objects.all()