from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

 

# Create your views here.

class HomePage(LoginRequiredMixin, ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    ordering = ['-date']
    paginate_by = 2


class ReadMore(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'blog/details.html'


class Share(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/form.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)