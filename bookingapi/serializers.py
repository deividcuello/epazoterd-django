from rest_framework import serializers
from .models import Booking
from users.models import AppUser
from users.serializers import UserSerializer

class BookingSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only = True)
    user_pk = serializers.PrimaryKeyRelatedField(queryset = AppUser.objects.all(), source = 'user', write_only = True, allow_null = True)

    class Meta:
        model = Booking
        fields = ["id", "phone", "date", "time", "time2", "booking_code", "additional_info", "people_no", "user", "user_pk"]