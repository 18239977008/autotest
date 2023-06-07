from django.test import TestCase
from apitest.views import home,login
from django.http import HttpRequest
# Create your tests here.
import pymysql
import urllib
import time,requests,re


class titlePageTest(TestCase):
    def test_loginpage_returne_title_html(self):
        request = HttpRequest()
        response = login(request)
        self.assertIn(b'test123456',response.content)