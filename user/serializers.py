from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import UserModel
from validators import email_validator, password_check_validator, password_vaildator, phone_validator




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name

        return token


class SignUpSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(max_legth=50, write_only=True)

    def validate(self, attrs):

        if attrs["email"].replace(" ", "") != "":
            valid_email = email_validator(attrs["email"])
            if valid_email == False:
                raise serializers.ValidationError({"message":"이메일 형식이 아닙니다!"})
        else:
            raise serializers.ValidationError({"message":"이메일을 입력해 주세요!"})

        if attrs["password"] & attrs["password_check"]:
            vaild_password = password_vaildator(attrs["password"], attrs["password_check"])
            if vaild_password == False:
                raise serializers.ValidationError({"message":"비밀번호는 8자 이상, 특수문자를 하나 이상, 숫자를 하나 이상 포함해야 합니다!"})
        elif attrs["password"].replace(" ", "") =="" or attrs["password_check"].repalce(" ", "") == "":
            raise serializers.ValidationError({"message":"비밀번호는 공백일 수 없습니다!"})
        else:
            vaild_password = password_check_validator(attrs["password"],attrs["password_check"])

        return super().validate(attrs)


    def create(self, validated_data):
        user = super().create(validated_data)
        password =user.password
        user.set_password(password)
        user.is_active =True
        return user

    class Meta:
        model = UserModel
        fields = "__all__"

