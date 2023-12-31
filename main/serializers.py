from rest_framework import serializers
from .models import Text_to_speech
from django.contrib.auth.models import User


class TextToSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text_to_speech
        fields = ['id', 'text', 'file_name']
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 
                  'first_name', 'last_name', 'password']