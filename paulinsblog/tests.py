from django.contrib.auth import get_user_model

#from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from . import views

#from django.utils import timezone
from .models import Post, UserProfile  #, Comment,
#from .forms import BlogForms, CommentForm
#from user.forms import UserRegForm, UpdateUserForm, ChangepassForm


# Create your tests here.

class Test_HomePage(TestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse ('home'))
        self.assertEquals(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse ('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h2 padding: 70px;><b>Articles</b></h2>')

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Nothing here')

class Test_New_Post(TestCase):

    def test_new_post_status_code(self):
        response = self.client.get('/new_post/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse ('new_post'))
        self.assertEqual(response.status_code, 200)

    def test_new_post_uses_correct_template(self):
        response = self.client.get(reverse ('new_post'))
        self.assertTemplateUsed(response, 'new_post.html')

    def test_new_post_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Nothing here')

class Test_Postdetails(TestCase):

    def test_postdetails_status_code(self):
        response = self.client.get('/postdetails/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_postdetails_uses_correct_template(self):
        response = self.client.get('/postdetails/<int:pk>/')
        self.assertTemplateUsed(response, 'postdetails.html')

    def test_postdetails_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Nothing here')

