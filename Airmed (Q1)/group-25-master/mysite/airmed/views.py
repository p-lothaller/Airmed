from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

def button(request):
    return render(request, 'airmed/fitness_page.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'airmed/main_menu.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'airmed/main_menu.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('main-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('main-home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('main-home')
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def fitness_page(request):
    return render(request, 'airmed/fitness_page.html', {'title': 'Fitness'})


def chest(request):
    return render(request, 'airmed/chest.html', {'title': 'chest ex'})

def back(request):
    return render(request, 'airmed/back.html', {'title': 'back ex'})

def legs(request):
    return render(request, 'airmed/legs.html', {'title': 'leg ex'})

def arms(request):
    return render(request, 'airmed/arms.html', {'title': 'arm ex'})
