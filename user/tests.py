from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from user.models import UserModel
# Create your tests here.
## 테스트 코드는 다른 코드에 의존해서 작성하면 안됨!!
## 한번 테스트 코드가 작동하고, 다른 테스트 코드가 작동할 때, DB가 초기화 되고 작동,
## 모든 테스트 코드는 stateless해야 한다!
class UserRegisterationAPIViewTestCase(APITestCase):
    def test_registeration(self):
        url = reverse("signup_view")
        user_data = {
            "email": "z9x80123@gmail.com",
            "password": "audgus1121!",
            "password_check": "audgus1121!",
            "profilename": "audgus"
        }
        response = self.client.post(url,user_data)
        self.assertEqual(response.status_code, 201)

class UserLoginAPIViewTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "email": "z9x80123@gmail.com",
            "password": "audgus1121!"
        }
        ## models.py의 create_user를 사용! ( override를 했기 때문! )
        self.user = UserModel.objects.create_user("z9x80123@gmail.com", "audgus", "audgus1121!")

    def test_login(self):
        response = self.client.post(reverse("login_view"),self.data)
        self.assertEqual(response.status_code, 200)

    def test_get_user_data(self):
        access_token = self.client.post(reverse("login_view"), self.data).data["access"]
        response = self.client.get(
            path=reverse("user_data_view"),
            HTTP_AUTHORIZATION= f"Bearer {access_token}"
        )
        self.assertEqual(response.status_code, 200)