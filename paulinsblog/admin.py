from django.contrib import admin
from .models import Post, UserProfile, Comment #import the new model created

admin.site.register(Post)  #Allows the posts to be visible in the admin area
admin.site.register(UserProfile)
admin.site.register(Comment)