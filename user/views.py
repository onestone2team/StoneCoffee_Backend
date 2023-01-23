from django.shortcuts import redirect
from rest_framework import permissions
from .models import UserModel
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.serializers import MyTokenObtainPairSerializer, SignUpSerializer , KakaoTokenObtainSerializer, PaymentuserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import get_object_or_404
from main.settings import KAKAO_CONFIG
import os
import time


# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입이 되었습니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"회원가입이 실패했습니다!"}, status=status.HTTP_400_BAD_REQUEST)


class UserData(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user_data = get_object_or_404(UserModel, request.user)
        serializer = PaymentuserSerializer(data=user_data)
        if serializer.is_vaild():
            return Response({"message":"회원의 정보입니다.", "data":f"{serializer.data}"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"잘못된 회원정보 입니다."}, status=status.HTTP_400_BAD_REQUEST)

kakao_login_uri = "https://kauth.kakao.com/oauth/authorize"
kakao_token_uri = "https://kauth.kakao.com/oauth/token"
user_uri = "https://kapi.kakao.com/v2/user/me"
class KakaoView(APIView):

    def get(self, request):

        client_key = KAKAO_CONFIG["KAKAO_REST_API_KEY"]
        redirect_uri = KAKAO_CONFIG["KAKAO_REDIRECT_URI"]

        uri = f"{kakao_login_uri}?client_id={client_key}&redirect_uri={redirect_uri}&response_type=code"

        return redirect(uri)

import requests

class KakaoTokenGet(APIView):

    def get(self, request):
        code = request.GET.get('code')

        if not code :
            error_description = request.GET.get('error_description')
            return Response({"message": error_description}, status=status.HTTP_400_BAD_REQUEST)

        client_key = KAKAO_CONFIG["KAKAO_REST_API_KEY"]
        redirect_uri = KAKAO_CONFIG["KAKAO_REDIRECT_URI"]

        request_parameter = {
            "grant_type": "authorization_code",
            "client_id": client_key,
            "redirect_uri": redirect_uri,
            "code": code,
        }
        token_headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        token_json = requests.post(kakao_token_uri, headers=token_headers, data=request_parameter).json()
        access_token = token_json["access_token"]
        access_token_hr = f"Bearer {access_token}"
        request_header = {
            'Authorization': access_token_hr,
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }

        get_user_info = requests.get(user_uri, headers=request_header).json()
        user_email = get_user_info["kakao_account"]["email"]
        profile_name = get_user_info["kakao_account"]["profile"]["nickname"]
        checkuser = UserModel.objects.filter(email = user_email)

        if checkuser:
            user = UserModel.objects.get(email = user_email)
            token=KakaoTokenObtainSerializer.get_token(user)
            login_refresh_token = str(token)
            login_access_token = str(token.access_token)
            res = Response(
                {
                    "message": "로그인 되었습니다.",
                    "access": login_access_token,
                    "refresh": login_refresh_token,
                    "kakao_access": access_token,
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            #유저 저장
            user = UserModel.objects.create()
            user.set_unusable_password()
            user.profilename = profile_name
            user.email = user_email

            #이미지 저장 없으면 기본 이미지
            if get_user_info["kakao_account"]["profile"]["profile_image_url"]:
                profile_image = get_user_info["kakao_account"]["profile"]["profile_image_url"]
                url = profile_image
                start = time.time()
                image_src = f"{profile_name}{start}.jpg"
                save_src = f"media/{profile_name}{start}.jpg"
                os.system(f"curl " + url + " > "+save_src)
                user.profile = image_src

            user.save()
            token=KakaoTokenObtainSerializer.get_token(user)
            login_refresh_token = str(token)
            login_access_token = str(token.access_token)
            res = Response(
                {
                    "message": "회원 가입 되었습니다.",
                    "access": login_access_token,
                    "refresh": login_refresh_token,
                },
                status=status.HTTP_200_OK,
            )
            return res


