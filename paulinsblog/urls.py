from django.urls import path
from .views import Home, PostDetails, New_Post, EditPost, DeletePost, NewComment # to import the different views we created

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('postdetails/<int:pk>/', PostDetails.as_view(), name='postdetails'),
    path('new_post/', New_Post.as_view(), name='new_post'),
    path('post/edit/<int:pk>/', EditPost.as_view(), name='edit'),
    path('post/<int:pk>/deletepost', DeletePost.as_view(), name='deletepost'),
    path('post/<int:pk>/newcomment/', NewComment.as_view(), name='newcomment'),
    
]
