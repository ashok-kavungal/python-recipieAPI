from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):
    def setUp(self):
        ''''setting up test user and test super'''
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='anu@gmail.com',
            password='123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='ashok@gmail.com',
            password='456abc',
            name='hisnameismathew'
        )

    def test_for_isUserListed(self):
        '''checking whether the user is listed in userlist'''
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)

    def test_user_page_changes(self):
        """Test whether the created user page allows changes"""
        url = reverse('admin:core_user_change', args=[self.user.id])#gets a dummy url for change in user page
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_add_newuser_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)        
