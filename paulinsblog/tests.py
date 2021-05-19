#from django.contrib.auth import get_user_model

#from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from . import views

#from django.utils import timezone
#from .models import Post, Comment, UserProfile
#from .forms import BlogForms, CommentForm
#from user.forms import UserRegForm, UpdateUserForm, ChangepassForm


# Create your tests here.


class Test_Postdetails(TestCase):

    def test_postdetails_status_code(self):
        response = self.client.get('/postdetails/<int:pk>/')
        self.assertEquals(response.status_code, 404)

    def test_view_url_by_name(self):
        response = self.client.get(reverse_lazy('postdetails/<int:pk>/'))
        self.assertEqual(response.status_code, 200)

    #def test_postdetails_uses_correct_template(self):
    #    response = self.client.get(reverse_lazy('/postdetails/<int:pk>/'))
    #    self.assertTemplateUsed(response, 'postdetails.html')

    def test_postdetails_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Nothing here')

