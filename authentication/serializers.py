from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

import os

from . import google


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ("username", "password")

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


# class GoogleSocialAuthSerializer(serializers.Serializer):
#     auth_token = serializers.CharField()

#     def validate_auth_token(self, auth_token):
#         user_data = google.Google.validate(auth_token)
#         try:
#             user_data['sub']
#         except:
#             raise serializers.ValidationError(
#                 'The token is invalid or expired. Please login again.'
#             )

#         if user_data['aud'] != settings.GOOGLE_CLIENT_ID:

#             raise AuthenticationFailed('oops, who are you?')

#         user_id = user_data['sub']
#         email = user_data['email']
#         name = user_data['name']
#         provider = 'google'

#         return register_social_user(
#             provider=provider, user_id=user_id, email=email, name=name)
