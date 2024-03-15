from rest_framework import serializers
from .models import Partner
from users.models import AppUser
from users.serializers import UserSerializer

class PartnerSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = True)
    user_pk = serializers.PrimaryKeyRelatedField(queryset = AppUser.objects.all(), source = 'user', write_only = True, allow_null = True)

    class Meta:
        model = Partner
        fields = ["id", "cv_file", "phone", "name", "message", "user", "user_pk"]