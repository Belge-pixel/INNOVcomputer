from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class StaffDashboardTests(TestCase):
    def setUp(self):
        # Create regular user
        self.regular_user = User.objects.create_user(username='user', password='pass')
        # Create staff user
        self.staff_user = User.objects.create_user(username='staff', password='pass', is_staff=True)
        self.client = Client()

    def test_dashboard_redirects_anonymous(self):
        response = self.client.get(reverse('staff:dashboard'))
        self.assertNotEqual(response.status_code, 200)
        self.assertIn(response.status_code, [302, 403])  # Redirect or forbidden

    def test_dashboard_access_for_staff(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get(reverse('staff:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/dashboard.html')
        self.assertContains(response, 'Dashboard Staff')

    def test_dashboard_forbidden_for_regular_user(self):
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('staff:dashboard'))
        self.assertNotEqual(response.status_code, 200)
        self.assertIn(response.status_code, [302, 403])

    def test_staff_home_access(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get(reverse('staff:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/home.html')

    def test_staff_home_forbidden_for_regular(self):
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('staff:home'))
        self.assertNotEqual(response.status_code, 200)
        self.assertIn(response.status_code, [302, 403])
