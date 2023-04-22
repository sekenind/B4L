from rest_framework import serializers
from . models import signin
from .models import signup

class signinSerializer(serializers.ModelSerializer):

    class Meta:
        model = signin
        fields = "__all__"

class signupSerializer(serializers.ModelSerializer):

    class Meta:
        model = signup
        fields = "__all__"