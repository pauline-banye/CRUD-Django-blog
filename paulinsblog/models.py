from django.db import models
from django.contrib.auth.models import User  # import the superuser
from django.utils import timezone # for the date/time
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField #added emojis and text editing capacity to the blog


class Post(models.Model): # Create new post model
   
    title = models.CharField(max_length=150)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = RichTextField(blank=True, null=True)
    intro = models.CharField(max_length=300)
    date_published = models.DateTimeField(default=timezone.now)
       

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('postdetails', args=(str(self.id)))


class UserProfile(models.Model): # Create user profile model
   
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile = RichTextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profilepics')
    website_url = models.CharField(max_length=250, null=True, blank=True)
    instagram_url = models.CharField(max_length=250, null=True, blank=True)
    linkedin_url = models.CharField(max_length=250, null=True, blank=True)
    facebook_url = models.CharField(max_length=250, null=True, blank=True)
    github_url = models.CharField(max_length=250, null=True, blank=True)
    twitter_url = models.CharField(max_length=250, null=True, blank=True)
    youtube_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    writer = models.CharField(max_length=250)
    review = models.TextField()
    commentdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.writer)



