from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import UserModel
from user.validators import email_validator, password_check_validator, password_vaildator, profile_name_validator, phone_validator, address_validator



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['profilename'] = user.profilename
        token['is_admin'] = user.is_admin

        return token

class KakaoTokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = cls.token_class.for_user(user)
        token['user_id'] = user.id
        token['profilename'] = user.profilename
        token['is_admin'] = user.is_admin
        return token

class SignUpSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(max_length=50, write_only=True)

    def validate(self, attrs):

        if attrs["email"].replace(" ", "") != "":
            valid_email = email_validator(attrs["email"])
            if valid_email == False:
                raise serializers.ValidationError({"message":"이메일 형식이 아닙니다!"})

        if attrs["password"].replace(" ", "") =="" or attrs["password_check"].replace(" ", "") == "":
            raise serializers.ValidationError({"message":"비밀번호는 공백일 수 없습니다!"})

        if attrs["password"] != "" and attrs["password_check"] != "":
            valid_password = password_vaildator(attrs["password"], attrs["password_check"])
            valid_password2 = password_check_validator(attrs["password"], attrs["password_check"])

            if valid_password == False:
                raise serializers.ValidationError({"message":"비밀번호는 8자 이상, 특수문자(@!%*#?&)를 하나 이상, 숫자를 하나 이상 포함해야 합니다!"})
            elif valid_password2 == False:
                raise serializers.ValidationError({"message":"비밀번호가 다릅니다"})

        # if attrs["profilename"]:
        #     valid_profilename = profile_name_validator(attrs["profilename"])
        #     if valid_profilename == False:
        #         raise serializers.ValidationError({"message":"프로필 이름은 4글자 이상, 특수문자는 _ 만 가능합니다"})

        attrs.pop("password_check", None)
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        password =user.password
        user.set_password(password)
        user.is_active =True
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = "__all__"


class ChangeUserInfoSerializer(serializers.ModelSerializer):
    # password_check = serializers.CharField(max_length=50, write_only=True)
    
    def validate(self, attrs):

        if attrs.get("address"):
            valid_address = address_validator(attrs["address"])
            if valid_address == False:
                raise serializers.ValidationError({"message":"주소 형식이 올바르지 않습니다"})

        if attrs.get("profilename"):
            valid_profilename = profile_name_validator(attrs["profilename"])
            if valid_profilename == False:
                raise serializers.ValidationError({"message":"프로필 이름은 4글자 이상, 특수문자는 _ 만 가능합니다"})

        if attrs.get("phone"):
            valid_phone = phone_validator(attrs["phone"])
            if valid_phone == False:
                raise serializers.ValidationError({"message":"전화번호는 - 문자 포함 010-1111-1111 형식입니다."})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.profile = validated_data.get('profile', instance.profile)
        instance.profilename = validated_data.get('profilename', instance.profilename)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

    class Meta:
        model = UserModel
        fields = ("profilename", "phone", "profile",  "address", "email")


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(max_length=50, write_only=True)
    password_check = serializers.CharField(max_length=50, write_only=True)


    def validate(self, attrs):
        if attrs.get("password") or attrs.get("password_check"):
            valid_password = password_vaildator(attrs["password"], attrs["password_check"])
            valid_password2 = password_check_validator(attrs["password"], attrs["password_check"])
            if valid_password == False:
                raise serializers.ValidationError({"message":"비밀번호는 8자 이상, 특수문자를 하나 이상, 숫자를 하나 이상 포함해야 합니다!"})
            elif valid_password2 == False:
                raise serializers.ValidationError({"message":"비밀번호가 다릅니다"})
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        if instance.check_password(validated_data.get('old_password')):
            instance.set_password(validated_data.get('password', instance.password))
            instance.save()
        else:
            raise serializers.ValidationError({"message":"기존 비밀번호가 다릅니다."})
        return instance
    
    class Meta:
        model = UserModel
        fields = ("password", "old_password", "password_check")


class PaymentuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"