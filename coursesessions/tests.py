from django.contrib.auth.models import User
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase

from coursesessions.models import CourseSession


class CourseSessionTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.user1.save()
        self.user2 = User.objects.create_user(
            username='maria', email='maria@…', password='top_secret')
        self.user2.save()

    def test_init_admin(self):
        login_response = self.c.post('/accounts/login/', {'username': 'jacob', 'password': 'top_secret'})
        assert login_response.status_code == 302

        response = self.c.post('/coursesessions/create_session/', {'session_name': 'test'})

        test_session = CourseSession.objects.get(pk=1)

        assert response.url == '/coursesessions/1/'

        assert len(CourseSession.objects.all()) == 1
        assert len(test_session.admins.all()) == 1
        assert self.user1 in test_session.admins.all()
        assert self.user2 not in test_session.admins.all()

