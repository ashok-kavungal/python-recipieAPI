from django import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):

    def setupForTest(self):
        '''setting up test user and test super'''
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

    def tes_for_isUserListed(self):
        '''checking whether the user is listed in userlist'''
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)
