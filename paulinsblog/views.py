from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # these are inbuilt class based views from Django to allow us view the list of posts on the blog (ListView), create a new blog post (CreateView), edit the contents of a post (UpdateView) and the details of each post (DetailView)
from .models import Post, Comment # for the Post and Comment models to be usable
from .forms import BlogForms, CommentForm #custom form created
from django.urls import reverse_lazy


class Home(ListView):
    model = Post
    template_name = 'home.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'postdetails.html'
    ordering = ['-date_published']


class New_Post(CreateView):
    model = Post
    form_class = BlogForms
    template_name = 'new_post.html'


class EditPost(UpdateView):
    model = Post
    form_class = BlogForms
    template_name = 'new_post.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')


class NewComment(CreateView):
    model = Comment
    form_class = CommentForm 
    template_name = 'newcomment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] 
        return super().form_valid(form) 

    success_url = reverse_lazy('home')


#    fields = '_all_'
#    fields = ('writer', 'review')