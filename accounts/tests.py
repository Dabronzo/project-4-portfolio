from django.test import TestCase
from django.urls import reverse
from agenda.models import Gig, Venue
from .models import NewUserDj
from datetime import date


class TestFormsViews(TestCase):
    """Test class for registration and log in views"""

    today = date.today()

    def setUp(self):
        # Creating a gig, user and venue for test#
        gig_a = Gig(event_name='testEvent', event_date=self.today)
        user_dj = NewUserDj(email='test@email', user_name='testDj')
        user_dj.is_staff = False
        user_dj.join_date = self.today
        user_dj_psw = 'some_123_password'
        self.user_dj_psw = user_dj_psw
        user_dj.set_password(user_dj_psw)
        user_dj.save()
        venue_test = Venue(
            name='TestVanue', address='TestAddress', city='TestCity', 
            venue_link='testLink'
            )
        venue_test.save()
        gig_a.dj = user_dj
        gig_a.slug = 'testEvent'
        gig_a.venue = venue_test
        gig_a.save()

        # selfing the objects
        self.gig_a = gig_a
        self.venue_a = venue_test

        # urls
        self.register_url = reverse('register')
        self.login_url = reverse('login')
    
    def test_user_created(self):
        """Testing if user is created"""
        user_count = NewUserDj.objects.all().count()

        self.assertEqual(user_count, 1)

    # url and template testing GET method
    def test_register_view_get(self):
        """Register template and url test"""
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_login_view_get(self):
        """Testing login template and url"""

        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_url_post(self):
        """Testing login template and url"""

        data = {'email': 'test@email', 'password': self.user_dj_psw}

        response = self.client.post(self.login_url, data, follow=True)
        status_code = response.status_code
        redirect_path = response.request.get('PATH_INFO')

        self.assertEqual(status_code, 200)
        self.assertEqual(redirect_path, "/")
