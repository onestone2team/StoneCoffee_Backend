from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class ChangeUserDataAPITestCase(APITestCase):
    def test_change_user_data(self):
        access_token = self.client.post(reverse("login_view"), self.data).data["access"]
        response = self.client.put(
            path=reverse("change_user_info_view"),
            HTTP_AUTHORIZATION=f"Bearer {access_token}",
    )