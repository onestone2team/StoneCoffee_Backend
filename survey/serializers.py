from rest_framework import serializers
from .models import Guest

class GuestIpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = "__all__"