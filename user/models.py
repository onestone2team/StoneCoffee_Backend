from django.db import models
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, profilename, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('User must have a password')
        # if not profilename:
        #     raise ValueError('User must have an profilename')

        instance = self.model(
            email=email,
            profilename=profilename
        )
        instance.set_password(password)
        instance.save(using=self._db)
        return instance

    def create_superuser(self, email, profilename, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        instance = self.create_user(
            email = email,
            password=password,
            profilename=profilename
        )
        instance.is_admin = True
        instance.save(using=self._db)
        return instance


class UserModel(AbstractBaseUser):
    email = models.EmailField('이메일', unique=True, error_messages={"unique":"이미 사용중인 이메일입니다"})
    password = models.CharField('비밀번호',max_length=30)
    profile = models.ImageField('프로필 사진',upload_to='%y/%m/', default='basic_profile/guest.png')
    profilename = models.CharField('회원이름',max_length=50, error_messages={"unique":"이미 사용중인 이름입니다"})
    address = models.TextField('배송지',blank=True, default="")
    phone = models.CharField('연락처',max_length=30,blank=True, default="")

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['profilename']

    def __str__(self):
        return self.profilename

    def has_perm(self, perm, obj=None):
        "Does the instance have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the instance have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the instance a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



