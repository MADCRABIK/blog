# импорт необходимых библиотек

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.


# View на основе класса. Возвращает object_list на основе модели в указанный шаблон.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


# View на основе класса. Возвращает object (или post) в указанный шаблон
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# View на основе класса. Возвращает form на основе fields из model в указанный шаблон
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


# View на основе класса. Возвращает form на основе fields из model в указанный шаблон
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
