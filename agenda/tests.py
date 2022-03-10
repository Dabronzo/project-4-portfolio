from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, timedelta, datetime
from .models import Gig, Venue
from accounts.models import NewUserDj


class TestNewGigsList(TestCase):
    """Test Class for the gig_view"""
    today = date.today()

    def setUp(self):
        # Creating a gig, user and venue for test#
        gig_a = Gig(event_name='testEvent', event_date=self.today)
        user_dj = NewUserDj(email='test@email', user_name='testDj')
        user_dj.is_staff = False
        user_dj.join_date = self.today
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

        # Create the client#
        self.client = Client()

        # Define URLS#
        self.home_list_url = reverse('home')
        self.detail_url = reverse('gig_detail', args=[gig_a.slug])

    def test_gigs_list(self):
        """Test the index/gigs_list view"""
        response = self.client.get(self.home_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_gig_detail(self):
        """Test the gig_detail view"""
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gig_detail.html')        





class TestGigSettings(TestCase):
    """Test Class for the gig models"""

    today = date.today()

    def setUp(self):
        gig_a = Gig(event_name='testEvent', event_date=self.today)
        user_dj = NewUserDj(email='test@email', user_name='testDj')
        user_dj.is_staff = False
        user_dj.join_date = self.today
        user_dj.save()
        venue_test = Venue(
            name='TestVanue', address='TestAddress', city='TestCity', 
            venue_link='testLink'
            )
        venue_test.save()
        gig_a.dj = user_dj
        gig_a.venue = venue_test
        gig_a.save()
        self.gig_a = gig_a

    def test_gig_status_default(self):
        """Testing default status"""
        self.assertEqual(self.gig_a.status, 0)

    def test_gig_days_to(self):
        yesterday = self.today - timedelta(days=1)
        yesterday_time = datetime.min.time()
        yesterday_datetime = datetime.combine(yesterday, yesterday_time)

        self.gig_a.event_date = yesterday_datetime
        days_to_test = self.gig_a.days_to

        self.assertEqual(days_to_test, -1)