from rest_framework import serializers
<<<<<<< HEAD

=======
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"
>>>>>>> 85acd5b6682cac49d30aef8ec9b3cf8e2172b26a
